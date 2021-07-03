from django.urls import path
from accounts.views import user_register

app_name = "accounts"

urlpatterns = [
    path('registration/', user_register, name='registration'),
]