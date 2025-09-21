from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

app_name = "accounts"

urlpatterns = [
    path("register/" , RegisterUserView.as_view(), name="register"),
    path("verify_otp/", VerifyUserOTPView.as_view(), name="verify-otp"),
    path("request_otp/" , RequestOTPView.as_view(), name="login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
