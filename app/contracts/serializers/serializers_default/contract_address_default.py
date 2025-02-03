from django.http import Http404
from web3 import Web3

__all__ = ['ContractAddressDefault']


class ContractAddressDefault:
    requires_context = True

    def __call__(self, field):
        value = field.parent.context['view'].kwargs['contract_address']
        if not Web3.is_address(value):
            raise Http404
        return value