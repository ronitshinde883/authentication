from django.contrib import admin
from django.urls import path,include
from . import views
from .views.auth_views import RegisterAPI,LoginAPI,LogoutAPI

urlpatterns = [
    path("api/register/", RegisterAPI.as_view(), name="api_register"),
    path("api/login/", LoginAPI.as_view(), name="api_login"),
    path("api/logout/", LogoutAPI.as_view(), name="api_logout")
]