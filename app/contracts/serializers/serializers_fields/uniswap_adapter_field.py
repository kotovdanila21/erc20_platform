from django.http import Http404
from rest_framework import serializers
from web3 import Web3

from app.contracts.web3 import ERC20UniswapAdapter

__all__ = ['UniswapAdapterField']

class UniswapAdapterField(serializers.HiddenField):
    def get_value(self, dictionary):
        contract_address = self.context["view"].kwargs['contract_address']
        if not Web3.is_address(contract_address):
            raise Http404
        return ERC20UniswapAdapter(contract_address)

    def __init__(self, **kwargs):
        kwargs['default'] = None
        super().__init__(**kwargs)