from django.urls import path
from .views import NewTrainee, ListTrainees, ListTrainee, ProfileTrainee

app_name = "core"

urlpatterns = [
    path("v1/newtrainee", NewTrainee.as_view(), name="newtrainee"),
    path("v1/trainees", ListTrainees.as_view(), name="trainees"),
    path("v1/trainee/<int:pk>/", ListTrainee.as_view(), name="trainee"),
    path("v1/traineeprofile/<int:pk>/", ProfileTrainee.as_view(), name="trainee_profile")
]

