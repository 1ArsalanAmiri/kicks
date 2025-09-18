from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path("request_otp/", RequestOTPView.as_view(), name="request-otp"),
    path("verify_otp/", VerifyOTPView.as_view(), name="verify-otp"),

    path("login/", RequestOTPView.as_view(), name="request-otp"),

]
