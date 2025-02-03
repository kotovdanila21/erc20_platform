from eth_utils import is_dict
from rest_framework import serializers

__all__ = ['ERC20TokenInfoSerializer', 'BaseERC20TokenInfoSerializer']

from app.contracts.serializers.serializers_default import ContractAddressDefault
from app.contracts.serializers.serializers_fields import Web3ContractField
from app.contracts.web3 import ERC20Adapter


class BaseERC20TokenInfoSerializer(serializers.Serializer):
    decimals = serializers.IntegerField(read_only=True)
    symbol = serializers.CharField(read_only=True)
    abi = serializers.JSONField(read_only=True)
    name = serializers.CharField(read_only=True)
    contract_address = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        if is_dict(instance):
            return super().to_representation(
                {
                    **instance,
                    **ERC20Adapter.fetch_contract_token_info(instance['contract'])
                }
            )
        return super().to_representation(
            ERC20Adapter.fetch_contract_token_info(instance)
        )

class ERC20TokenInfoSerializer(BaseERC20TokenInfoSerializer):
    contract_address = serializers.CharField(default=ContractAddressDefault())
    contract = Web3ContractField()

    def validate(self, attrs):
        if not ERC20Adapter.is_token_contract(attrs['contract']):
            raise serializers.ValidationError({'detail': 'Invalid token contract address.'})
        return super().validate(attrs)