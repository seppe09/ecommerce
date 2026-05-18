from django.shortcuts import redirect
from django.contrib import messages

def seller_required(view_function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        if not request.user.is_seller:
            messages.error(request, "You are not authorized to visit this page")
            return redirect("dashboard")
        return view_function(request, *args, **kwargs)
    return wrapper