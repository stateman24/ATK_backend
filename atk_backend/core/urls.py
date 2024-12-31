from django.urls import path
from .views import ListTrainees, ListTrainee, ProfileTrainee, UpdateDeleteTrainee, UpdateDeleteProfileTrainee, trainee_report

app_name = "core"

urlpatterns = [
    path("v1/trainees", ListTrainees.as_view(), name="trainees"),
    path("v1/trainee/<int:pk>/", ListTrainee.as_view(), name="trainee"),
    path("v1/traineeprofile/<int:pk>/", ProfileTrainee.as_view(), name="trainee_profile"),
    path("v1/trainee/<int:pk>", UpdateDeleteTrainee.as_view(), name="update_delete_trainee"),
    path('v1/traineeprofile/<int:pk>/', UpdateDeleteProfileTrainee.as_view(), name="update_delete_profile_trainee"),
    path("traineereport/", trainee_report, name="trainee_report"),
]

