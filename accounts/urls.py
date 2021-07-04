from django.urls import path
from accounts.views import UserRegisterView

app_name = "accounts"

urlpatterns = [
    path('registration/', UserRegisterView, name='registration'),
]