from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings

USER_TYPE_CHOICES = [
    ('procurement_admin', 'Procurement Admin'),
    ('supplier', 'Supplier'),
]

ORDER_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]

PAYMENT_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('failed', 'Failed'),
    ('refunded', 'Refunded'),
]

PAYMENT_METHOD_CHOICES = [
    ('credit_card', 'Credit Card'),
    ('paypal', 'PayPal'),
    ('bank_transfer', 'Bank Transfer'),
    ('cash', 'Cash'),
]

class Account(AbstractUser):
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='supplier')

    def __str__(self):
        return self.username
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    product = models.ManyToManyField(Product)  
    quantity = models.PositiveIntegerField()  
    request_date = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')  
    approval_date = models.DateTimeField(blank=True, null=True)  
    comments = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"Request by {self.user.username} for {self.product}"
    
class OrderRefund(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  
    reason = models.TextField(blank=True, null=True)  
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2) 
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')  
    request_date = models.DateTimeField(auto_now_add=True)  
    approval_date = models.DateTimeField(blank=True, null=True) 
    comments = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"Refund for Order {self.order.id} by {self.user.username}"

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment {self.id} for Order {self.order.id} by {self.user.username}"