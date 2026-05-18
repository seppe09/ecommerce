<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.utils import extract_post_data
from .models import Product, Category
from apps.decorators import seller_required, superuser_required

@superuser_required
def create_category(request):
    category = Category.objects.create(
        name="Electronics",
    )
    print(category)
    return redirect("dashboard")

@seller_required
def product_list_view(request):
    products = Product.objects.filter(seller=request.user).order_by("-created_at")
    return render(request, "products/product_list.html", {"products": products})

from django.utils.text import slugify

@seller_required
def add_product_view(request):
    categories = Category.objects.all()
    if request.method == "POST":
        fields = ["product_category", "title", "price", "description", "stock"]
        data = extract_post_data(request, *fields)
        
        image = request.FILES.get("image")
        is_available = request.POST.get("is_available") == "on"
        
        try:
            category = Category.objects.get(id=data["product_category"])
            
            # Generate unique slug
            slug = slugify(data["title"])
            if Product.objects.filter(slug=slug).exists():
                import uuid
                slug = f"{slug}-{uuid.uuid4().hex[:8]}"

            product = Product.objects.create(
                product_category=category,
                title=data["title"],
                slug=slug,
                image=image,
                price=data["price"],
                description=data["description"],
                stock=data["stock"],
                is_available=is_available,
                seller=request.user,
            )
            print(product)
            messages.success(request, f"Product '{product.title}' added successfully!")
            return redirect("product_list")
        except Exception as e:
            messages.error(request, f"Error adding product: {str(e)}")
            
    return render(request, "products/add_product.html", {"categories": categories})
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037
