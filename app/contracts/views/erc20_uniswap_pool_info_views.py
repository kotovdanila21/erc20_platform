from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app.contracts.serializers import ERC20UniswapInfoSerializer

__all__ = ['ERC20UniswapPoolInfoView']


class ERC20UniswapPoolInfoView(GenericAPIView):
    serializer_class = ERC20UniswapInfoSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)