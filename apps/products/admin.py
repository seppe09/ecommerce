from django.contrib import admin
<<<<<<< HEAD
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "seller", "product_category", "price", "stock", "is_available")
    list_filter = ("is_available", "product_category", "seller")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
=======

# Register your models here.
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037
