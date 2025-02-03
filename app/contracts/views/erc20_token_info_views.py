from rest_framework.generics import GenericAPIView

__all__ = ['ERC20TokenInfoView']

from rest_framework.response import Response
from app.contracts.serializers import ERC20TokenInfoSerializer


class ERC20TokenInfoView(GenericAPIView):
    serializer_class = ERC20TokenInfoSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)