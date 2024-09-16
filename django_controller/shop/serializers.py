from rest_framework import serializers
from .models import Product, CustomUser

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source='seller.username')  # Display seller username

    class Meta:
        model = Product
        fields = ['id', 'seller', 'name', 'description', 'price', 'stock', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'balance']
