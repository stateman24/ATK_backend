from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = "user_auth"

urlpatterns = [
    path("v1/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/login/refresh/", TokenRefreshView.as_view(), name="token_refresh")
]
