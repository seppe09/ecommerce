from django.db import models
from ..accounts.models import BaseModel
from django.conf import settings

class Category(BaseModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return self.name

class Product(BaseModel):
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name="products")
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="products")
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="products/", blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.seller.full_name}"
    

