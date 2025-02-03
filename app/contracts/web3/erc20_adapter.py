import asyncio
import typing
from functools import lru_cache

import requests
from asgiref.sync import async_to_sync
from web3 import Web3, HTTPProvider
from web3.contract import Contract
from web3.exceptions import ABIFunctionNotFound, Web3ValueError, MismatchedABI, Web3Exception

from api import settings

__all__ = ['ERC20Adapter']


class ERC20Adapter:
    def __init__(self):
        self.w3 = self.get_web3()

    @staticmethod
    def get_web3() -> Web3:
        return Web3(HTTPProvider(settings.ERC20_PROVIDER_URL))

    def get_contract(self, contract_address, abi=None) -> Contract:
        if abi is None:
            abi = self.get_contract_abi(contract_address)
        return self.w3.eth.contract(
            Web3.to_checksum_address(contract_address),
            abi=abi
        )

    @staticmethod
    def is_token_contract(contract) -> bool:
        try:
            contract.get_function_by_name('decimals')
            return True
        except Web3Exception:
            return False

    @staticmethod
    def safe_contract_function_call(contract: Contract, function_name, default_value=None):
        try:
            return contract.get_function_by_name(function_name)().call()
        except Web3Exception as e:
            return default_value

    @staticmethod
    def fetch_contract_token_info(contract: Contract) -> dict:
        return {
            'contract_address': contract.address,
            'abi': contract.abi,
            'decimals': ERC20Adapter.safe_contract_function_call(contract, 'decimals', -1),
            'name': ERC20Adapter.safe_contract_function_call(contract, 'name'),
            'symbol': ERC20Adapter.safe_contract_function_call(contract, 'symbol'),
        }

    @classmethod
    def cls_get_contract(cls, contract_address) -> Contract:
        return cls().get_contract(contract_address)

    @staticmethod
    @lru_cache()
    def get_contract_abi(contract_address) -> typing.Union[typing.List[dict], None]:
        url = (
            f'{settings.ETHERSCAN_API_URL}/api?'
            f'module=contract'
            f'&action=getabi'
            f'&address={contract_address}'
            f'&apiKey={settings.ETHERSCAN_API_KEY}'
        )
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['result']
