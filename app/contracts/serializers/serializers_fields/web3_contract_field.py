from rest_framework import serializers
from app.contracts.web3 import ERC20Adapter

__all__ = ['Web3ContractField']

class Web3ContractField(serializers.HiddenField):
    def get_value(self, dictionary):
        contract_address = self.context["view"].kwargs['contract_address']
        return ERC20Adapter.cls_get_contract(contract_address)

    def __init__(self, **kwargs):
        kwargs['default'] = None
        super().__init__(**kwargs)