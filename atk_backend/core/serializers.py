from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TraineeProfile

class TranieeProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TraineeProfile
        fields = ["age", "phone_number", "department", "level", "belt_rank"]


class UserSerilaizer(serializers.ModelSerializer):
    trainee_profile = TranieeProfileSerilizer()
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "date_joined", "trainee_profile"]    

    def create(self, validated_data):
        profile_data = validated_data.pop('trainee_profile')
        user = User.objects.create(**validated_data)
        TraineeProfile.objects.create(user=user, **profile_data)
        return user
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop("trainee_profile")
        profile = instance.trainee_profile
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        profile.age = profile_data.get("age", profile.age)
        profile.phone_number = profile_data.get("phone_number", profile.phone_number)
        profile.department = profile_data.get("department", profile.department)
        profile.level = profile_data.get("level", profile.level)
        profile.belt_rank = profile_data.get("belt_rank", profile.belt_rank)
        profile.save()
        return instance

        