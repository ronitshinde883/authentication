from rest_framework import serializers
from .models import Userprofile
from django.contrib.auth.models import User

class Registerserializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Userprofile
        fields =['username', 'email', 'password', 'phone']
        
    def create(self,validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # 🔥 create profile
        profile = Userprofile.objects.create(
            user=user,
            **validated_data
        )

        return profile