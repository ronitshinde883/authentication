from ..serializers.auth_serializer import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login as auth_login, authenticate,logout
from django.contrib.auth.models import User


#will be updating to jwt based authentication later
class RegisterAPI(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"User registered successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPI(APIView):
    def post(self,request):
        email=request.data.get("email")
        password=request.data.get("password")
        
        try:
            user_obj=User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                "error":"Invalid Email Or Password"
            },status=status.HTTP_401_UNAUTHORIZED)
        user=authenticate(username=user_obj.username,password=password)
        
        if user:
            return Response({
                "message":"Login succesful"
            },status=status.HTTP_200_OK)
            
        return Response(
            {"error": "Invalid email or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )
class LogoutAPI(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        logout(request)
        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_200_OK
        )