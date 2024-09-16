from rest_framework import permissions

class IsSellerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only sellers to create, update, or delete their own products.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the seller of the product
        return request.user.is_authenticated and request.user.is_seller()

class IsCustomerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow customers to interact with the cart.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_customer()
