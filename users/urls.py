from django.urls import path
from .views import user_register, user_login, user_logOut, user_check_profile, reset_password, activate_account

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logOut, name='logout'),
    path('profile/', user_check_profile, name='profile'),
    path('password-reset/', reset_password, name='password_reset_request'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate_account'),  # New activation route
]
