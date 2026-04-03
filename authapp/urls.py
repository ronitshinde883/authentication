from django.contrib import admin
from django.urls import path,include
from . import views
from .views.auth_views import RegisterAPI

urlpatterns = [
    path("api/register/", RegisterAPI.as_view(), name="api_register"),
]