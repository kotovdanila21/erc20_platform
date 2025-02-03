from rest_framework import serializers

from app.contracts.serializers.serializers_default import ContractAddressDefault
from app.contracts.serializers.serializers_fields import UniswapAdapterField
from app.contracts.web3 import ERC20UniswapAdapter
from app.contracts.serializers import BaseERC20TokenInfoSerializer

__all__ = ['ERC20UniswapInfoSerializer']


class ERC20UniswapInfoSerializer(serializers.Serializer):
    quote_token = BaseERC20TokenInfoSerializer(read_only=True)
    base_token = BaseERC20TokenInfoSerializer(read_only=True)
    adapter = UniswapAdapterField()

    def validate(self, attrs):
        if not attrs['adapter'].is_valid():
            raise serializers.ValidationError({
                'detail': 'Invalid uniswap contract address.'
            })
        return super().validate(attrs)

    def to_representation(self, instance):
        adapter = instance['adapter']
        return super().to_representation({
            **instance,
            **{
                'base_token': adapter.get_base_token_contract(),
                'quote_token': adapter.get_quote_token_contract(),
            }
        })

    class Meta:
        help_text = 'Serializer for Uniswap pair token information'
