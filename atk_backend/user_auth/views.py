from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from core.serializers import UserSerilaizer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny


# create new traniee 
class RegisterTrainee(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilaizer
    permission_classes = [AllowAny]
