from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path("register/" , RegisterUserView.as_view(), name="register"),
    path("verify_otp/", VerifyUserOTPView.as_view(), name="verify-otp"),
    path("request_otp/" , RequestOTPView.as_view(), name="login"),

]
