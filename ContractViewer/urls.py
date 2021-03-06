"""ContractViewer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.urls import urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from contracts.views import insert_data, homepage, ContractSearchView
from accounts.views import dashboard
from accounts.views import dashboard, UserResetPasswordView


urlpatterns = [
    path('', homepage, name='homepage'),
    path('insert_data/', insert_data, name='insert_data'),
    path('search_contracts/', ContractSearchView.as_view(), name='search_contracts'),
    path('admin/', admin.site.urls),
    path('contracts/', include('contracts.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/password_reset/', UserResetPasswordView.as_view(), name='password_reset'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('oauth/', include("social_django.urls", namespace='social')),
    path('oauth/complete/github/dashboard/', dashboard, name='dashboard'),
]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

