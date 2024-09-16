from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class CustomUser(AbstractUser):
    SELLER = 'Seller'
    CUSTOMER = 'Customer'
    VISITOR = 'Visitor'
    ROLE_CHOICES = [
        (SELLER, 'Seller'),
        (CUSTOMER, 'Customer'),
        (VISITOR, 'Visitor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=VISITOR)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # For customer balance

    def is_seller(self):
        return self.role == self.SELLER

    def is_customer(self):
        return self.role == self.CUSTOMER

    def is_visitor(self):
        return self.role == self.VISITOR
