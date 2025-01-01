from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterTrainee, LogoutView


app_name = "user_auth"

urlpatterns = [
    path("v1/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("v1/register/", RegisterTrainee.as_view(), name="resgister"),
    path("v1/logout/", LogoutView.as_view(), name="logout")
]
