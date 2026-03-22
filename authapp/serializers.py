from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User

class Registerserializer(serializers.ModelSerializer):
    phone=serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields=['username', 'email', 'password', 'phone']
        