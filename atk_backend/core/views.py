from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerilaizer
from rest_framework.permissions import AllowAny, IsAdminUser

# NOTE : Admin password: atkadmin

# create new traniee 
class NewTrainee(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilaizer
    permission_classes = [AllowAny]

# list all trainees 
class ListTrainees(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilaizer
    permission_classes = [AllowAny]

# list a single trainee
class ListTrainee(generics.RetrieveAPIView):
    serializer_class = UserSerilaizer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

