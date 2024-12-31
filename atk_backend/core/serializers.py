from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TraineeProfile

class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", 'username', "first_name", "last_name", "email", "date_joined",]


class TranieeProfileSerilizer(serializers.ModelSerializer):
    traninee = UserSerilaizer(read_only=True)

    class Meta:
        model = TraineeProfile
        fields = ["trainee", "age", "phone_number", "department", "level", "belt_rank"]
