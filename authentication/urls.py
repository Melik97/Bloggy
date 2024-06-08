from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import GoogleLoginApi, TokenController

urlpatterns = [
      path('', TokenController.as_view(), name='token_obtain_pair'),
      path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      path("auth/", GoogleLoginApi.as_view(), name="login-with-google"),
]

