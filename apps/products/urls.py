from django.urls import path
from .views import product_list_view, add_product_view, create_category

urlpatterns = [
    path("create_category/", create_category,name="create_category"),
    path("product_list/", product_list_view, name="product_list"),
    path("add_product/", add_product_view, name="add_product"),
]