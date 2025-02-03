import json
import os.path

from app.contracts.web3 import ERC20Adapter

__all__ = ['ERC20UniswapAdapter']

class ERC20UniswapAdapter:
    def __init__(self, contract_address):
        self.erc20_adapter = ERC20Adapter()
        self.contract = self.erc20_adapter.get_contract(
            contract_address,
            abi=self.get_abi()
        )

    @staticmethod
    def get_abi():
        with open(os.path.join('abi', 'uniswap_abi.json'), mode='r') as f:
            return json.load(f)

    def get_base_token_contract(self):
        return self._execute_uniswap_call('token0')

    def get_quote_token_contract(self):
        return self._execute_uniswap_call('token1')

    def _execute_uniswap_call(self, func: str):
        return self.erc20_adapter.get_contract(
            self.erc20_adapter.safe_contract_function_call(self.contract, func)
        )

    def _fetch_pool_token(self, token_contract_address):
        token_contract = self.erc20_adapter.get_contract(token_contract_address)
        return self.erc20_adapter.fetch_contract_token_info(token_contract)

    def is_valid(self) -> bool:
        result = self.erc20_adapter.safe_contract_function_call(
            self.contract, 'token0', 1
        )
        return not isinstance(result, int)