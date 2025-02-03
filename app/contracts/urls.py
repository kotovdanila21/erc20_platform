from django.urls import path
from .views import ERC20TokenInfoView, ERC20UniswapPoolInfoView

urlpatterns = [
    path('erc20/token/<str:contract_address>/', ERC20TokenInfoView.as_view(), name='erc20_token_info'),
    path('erc20/uniswap/<str:contract_address>/', ERC20UniswapPoolInfoView.as_view(), name='erc20_uniswap_info'),
]