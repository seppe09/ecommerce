from django.shortcuts import render, redirect, get_object_or_404
from ..models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from apps.utils import extract_post_data

def register_user_view(request):
    if request.method == "POST":
        fields = ["seller_type","first_name","middle_name","last_name","username","email","password","confirm_password",]
        data = extract_post_data(request, *fields)

        if not data["username"]:
            messages.error(request, "Please enter a username.")
            return render(request, "accounts/auth_pages/register_user.html", {"data": data})

        if data["password"] != data["confirm_password"]:
            messages.error(request, "Password and confirm password do not match.")
            return render(request, "accounts/auth_pages/register_user.html", {"data": data})
            
        if User.objects.filter(username=data["username"]).exists():
            messages.error(request, "User with this username already exists. Choose a different username.")
            return render(request, "accounts/auth_pages/register_user.html", {"data": data})

        user = User.objects.create_user(
            is_seller=data["seller_type"],
            first_name=data["first_name"],
            middle_name=data["middle_name"],
            last_name=data["last_name"],
            username=data["username"],
            email=data["email"],
            password=data["password"],
        )

        login(request, user)
        return redirect("dashboard")
        
    return render(request, "accounts/auth_pages/register_user.html")

def login_user_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        data = extract_post_data(request,
            "username",
            "password",
        )
        if User.objects.filter(username=data["username"], is_deleted=True):
            messages.error(request, "No user exists with this username.")
            return render(request, "accounts/auth_pages/login_user.html")
    
        if not data["username"] or not data["password"]:
            messages.error(request, "Please provide both username and password.")
            return render(request, "accounts/auth_pages/login_user.html")

        user = authenticate(request, username=data["username"], password=data["password"])
        if user is not None:
            messages.success(request, f"Welcome back {user.username}")
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")
        return render(request, "accounts/auth_pages/login_user.html")
        
    return render(request, "accounts/auth_pages/login_user.html")

@login_required      
def dashboard_view(request):
    return render(request, "accounts/auth_pages/dashboard.html")

@login_required
def logout_user_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been successfully logged out.")

    return redirect("login")

@login_required
def delete_user_view(request, pk):
    user = request.user
    verification = f"{user.username}/I confirm this deletion"
    if request.method == "POST":
        fields = ["reason","confirmation", "password"]
        data = extract_post_data(request, *fields)

        if not data:
            messages.error(request, "Please provide required data.")
            return render(request, "accounts/auth_pages/delete_user.html")
        
        elif data and data["reason"] and data["confirmation"] and data["password"]:
            if verification == data["confirmation"]:
                user = authenticate(request, username=user.username, password=data["password"])
                if user:
                    logout(request)
                    user.is_deleted = True
                    user.save()
                    messages.success(request, "Account deleted successfully.")
                    return redirect("login")
                else:
                    messages.error(request, "Username or Password is wrong.")
                    return redirect("delete_user", pk=pk)
                
            return redirect("delete_user", pk=pk)
        
    return render(request, "accounts/auth_pages/delete_user.html", {
        "verification": verification,
    })

def recover_user_view(request):
    if request.method == "POST":
        fields = ["email","username","password"]
        data = extract_post_data(request, *fields)
        user = User.objects.filter(email=data["email"], username=data["username"], is_deleted=True).first()

        if not user:
            messages.error(request, f"We do not have any user linked to this {data['email']}.")
            return redirect("recover_user")

        if not user.check_password(data["password"]):
            messages.error(request, "Incorrect password")
            return redirect("recover_user")
        
        user.is_deleted = False
        user.save()
        messages.success(request, "Your account recovery was successfull try login.")
        return redirect("login")
    
    return render(request, "accounts/auth_pages/recover_user.html")

            
        


        
