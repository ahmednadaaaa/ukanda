from django.db import models
from store.models import Cart

# Create your models here.


class Info(models.Model):
    place =models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=400)

    def __str__(self):
        return self.email


class Invoice(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.first_name