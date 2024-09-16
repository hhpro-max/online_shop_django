from rest_framework import generics, permissions,views
from rest_framework.response import Response
from .models import Product , CustomUser
from .serializers import ProductSerializer , UserSerializer
from .permissions import IsSellerOrReadOnly ,IsCustomerOrReadOnly

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSellerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSellerOrReadOnly]

class ShoppingCartView(views.APIView):
    permission_classes = [IsCustomerOrReadOnly]

    def post(self, request):
        product_id = request.data.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        if product.stock > 0:
            # logic here
            return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)
        return Response({'error': 'Product out of stock'}, status=status.HTTP_400_BAD_REQUEST)

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer 