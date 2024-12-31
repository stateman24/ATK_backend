from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerilaizer, TranieeProfileSerilizer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .models import TraineeProfile
from rest_framework_simplejwt.authentication import JWTAuthentication

# NOTE : Admin password: atkadmin

# create new traniee 
class NewTrainee(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilaizer
    permission_classes = [AllowAny]

# list all trainees 
class ListTrainees(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.prefetch_related("trainee_profile")
    serializer_class = UserSerilaizer
    permission_classes = [IsAuthenticated]

class UpdateDeleteTrainee(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.prefetch_related("trainee_profile")
    serializer_class = UserSerilaizer
    permission_classes = [IsAuthenticated]

# list a single trainee
class ListTrainee(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerilaizer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

class ProfileTrainee(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = TranieeProfileSerilizer
    permission_classes = [IsAuthenticated]
    queryset = TraineeProfile.objects.all()

class UpdateDeleteProfileTrainee(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = TranieeProfileSerilizer
    permission_classes = [IsAuthenticated]
    queryset = TraineeProfile
