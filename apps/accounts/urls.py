from django.urls import path
<<<<<<< HEAD
from .views.auth_views import register_user_view, login_user_view, dashboard_view, logout_user_view, delete_user_view, recover_user_view
from .views.profile_views import view_profile, edit_profile

urlpatterns = [
    path("register/", register_user_view, name="register"),
    path("login/", login_user_view, name="login"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("logout/", logout_user_view, name="logout"),
    path("delete/<int:pk>/", delete_user_view, name="delete_user"),
    path("recover/", recover_user_view, name="recover_user"),
    path("profile/", view_profile, name="view_profile"),
    path("profile/edit/", edit_profile, name="edit_profile"),
=======

urlpatterns = [
    
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037
]