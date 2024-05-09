from django.db import models
from django.contrib.auth.models import User

class CustomerManager(models.Manager):
    def create_customer(self, first_name, last_name, email, phone_number, address):
        customer = self.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
        )
        return customer

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)  

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.PositiveIntegerField(default=0)  
    image = models.ImageField(upload_to="image")

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.BigIntegerField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

class CartItems(models.Model):  # Changed 'CartItems' to 'CartItem' and indented
        product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Changed 'Product' to 'product'
        quantity = models.PositiveBigIntegerField(default=0)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'{self.quantity}*{self.product.name}'

