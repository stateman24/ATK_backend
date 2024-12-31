from django.db import models
from django.contrib.auth.models import User

class TraineeProfile(models.Model):

    # trainee's student level e.g. 100 level for first year
    class Level(models.IntegerChoices):
        PART_1 = 100, "100_level"
        PART_2 = 200, "200_level"
        PART_3 = 300, "300_level"
        PART_4 = 400, "400_level"
        PART_5 = 500, "500_lavel"

    # trainee belt rank in the club
    class BeltRank(models.TextChoices):
        WHITE = "White", "White"
        BLUE = "Blue", "Blue"
        GREEN = "Green", "Green"
        PURPLE = "Purple", "Purple"
        BLACK = "Black", "Black"
        BROWN = "Brown", "Brown"
        RED = "Red", "Red"
        ORANGE = "Orange", "Orange"
        YELLOW = "Yellow", "Yellow"


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    age = models.IntegerField(blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    deparment = models.CharField(max_length=100, blank=False)
    level = models.IntegerField(choices=Level, default=Level.PART_1)
    belt_rank = models.CharField(max_length=225, choices=BeltRank, default=BeltRank.WHITE)


    class Meta:
        def __str__(self):
            return  "Traniee Profile"
