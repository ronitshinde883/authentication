from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Userprofile
from .serializers import Registerserializer
from rest_framework.generics import CreateAPIView
# Create your views here.

class RegisterView(CreateAPIView):
    queryset = Userprofile.objects.all()
    serializer_class =Registerserializer