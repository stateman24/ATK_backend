from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerilaizer, TranieeProfileSerilizer
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import TraineeProfile

# NOTE : Admin password: atkadmin

# create new traniee 
class NewTrainee(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilaizer
    permission_classes = [AllowAny]

# list all trainees 
class ListTrainees(generics.ListAPIView):
    queryset = User.objects.prefetch_related("trainee_profile")
    serializer_class = UserSerilaizer
    permission_classes = [AllowAny]

# list a single trainee
class ListTrainee(generics.RetrieveAPIView):
    serializer_class = UserSerilaizer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

class ProfileTrainee(generics.RetrieveAPIView):
    serializer_class = TranieeProfileSerilizer
    permission_classes = [AllowAny]
    queryset = TraineeProfile.objects.all()

class UpdateTranieeProfile(generics.RetrieveUpdateAPIView):
    queryset = TraineeProfile.objects.all()
    serializer_class = TranieeProfileSerilizer
    permission_classes = [AllowAny]

class DeleteTraineeProfile(generics.RetrieveDestroyAPIView):
    serializer_class = TranieeProfileSerilizer
    permission_classes = [AllowAny]
    queryset = TraineeProfile.objects.all()
