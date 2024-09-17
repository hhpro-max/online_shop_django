from rest_framework import serializers
from .models import Product, CustomUser

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source='seller.username')  # Display seller username

    class Meta:
        model = Product
        fields = ['id', 'seller', 'name', 'description', 'price', 'stock', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'role', 'balance']
    
    def create(self, validated_data):
        # Use the create_user method to handle password hashing
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],  # Hashes the password
            role=validated_data.get('role', CustomUser.VISITOR),  # Default role is VISITOR
        )
        return user