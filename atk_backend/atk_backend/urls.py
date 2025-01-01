from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("core.urls", namespace="core")),
    path("api/auth/", include("user_auth.urls", namespace="user_auth")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swaggerdocs", SpectacularSwaggerView.as_view(), name="swagger-ui")
]
