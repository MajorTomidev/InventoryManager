from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

# CATEGORY MODEL--------------------------------------------------------------------------------
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')
     

# MANUFACTURER MODEL--------------------------------------------------------------------------------
class Manufacturer(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    products_quantity = models.PositiveIntegerField()
    location = models.TextField()
    contact_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Manufacturer')
        verbose_name_plural = ('Manufacturers')
        

# PRODUCT MODEL--------------------------------------------------------------------------------------
class Product(models.Model):
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='my_products', on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models. DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Product')
        verbose_name_plural = ('Products')
        ordering = ['-created']

# ORDER MODEL--------------------------------------------------------------------------------------------
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=250)
    payment_status = models.BooleanField(default=False)
    delivery_status = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = ('Order')
        verbose_name_plural = ('Orders')
        ordering = ['-created']
