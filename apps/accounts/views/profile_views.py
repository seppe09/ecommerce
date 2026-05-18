from django.shortcuts import render, redirect, get_object_or_404  
from ..models import User, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.utils import extract_post_data

@login_required
def view_profile(request):
    # Ensure profile exists for the user
    profile, created = Profile.objects.get_or_create(user=request.user)
    context = {
        "profile": profile
    }
    return render(request, "accounts/profile_pages/view_profile.html", context)

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    user = request.user
    
    if request.method == "POST":
        fields = ["first_name", "last_name", "middle_name", "email", "gender", "bio", "date_of_birth"]
        data = extract_post_data(request, *fields)
        
        # Update User data
        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        user.middle_name = data.get("middle_name", user.middle_name)
        user.email = data.get("email", user.email)
        user.save()
        
        # Update Profile data
        profile.gender = data.get("gender", profile.gender)
        profile.bio = data.get("bio", profile.bio)
        
        dob = data.get("date_of_birth")
        if dob:
            profile.date_of_birth = dob
            
        if "profile_image" in request.FILES:
            profile.profile_image = request.FILES["profile_image"]
            
        profile.save()
        messages.success(request, "Your profile has been updated successfully!")
        return redirect("view_profile")
        
    context = {
        "profile": profile,
        "user": user,
        "genders": Profile.GENDER
    }
    return render(request, "accounts/profile_pages/edit_profile.html", context)
