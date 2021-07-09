from django.urls import path, include
from accounts.views import UserRegisterView, dashboard, UserResetPasswordView

app_name = "accounts"

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('login/dashboard/', dashboard, name='dashboard'),
    path('logout/dashboard/', dashboard, name='dashboard'),
    path('registration/', UserRegisterView.as_view(), name='registration'),
]
