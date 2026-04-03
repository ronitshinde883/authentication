from django.contrib import admin

# Register your models here.
from .models.auth_model import Userprofile,User

admin.site.register(Userprofile)