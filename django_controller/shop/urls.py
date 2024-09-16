from django.urls import path
from .views import ProductListCreate, ProductDetail, ShoppingCartView, UserCreateView

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('cart/', ShoppingCartView.as_view(), name='shopping-cart'),
    path('register/', UserCreateView.as_view(), name='user-register'),
]
