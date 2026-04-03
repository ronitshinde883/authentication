from rest_framework import serializers
from ..models.auth_model import Userprofile
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    phone=serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields=["username","email","password","phone"]
        extra_kwargs = {
            'password': {'write_only': True}
            
        }
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
    
    def create(self, validated_data):
        phone=validated_data.pop("phone")
        
        user=User.objects.create_user(**validated_data)
        
        Userprofile.objects.create(
            user=user,
            phone=phone
        )
        return user