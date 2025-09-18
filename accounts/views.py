from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RequestOTPSerializer, VerifyOTPSerializer
from .models import EmailOTP, User
from django.core.mail import send_mail
from django.conf import settings
from secrets import randbelow



class RequestOTPView(generics.GenericAPIView):
    serializer_class = RequestOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        if not email:
            return Response({"error": "Email is required"}, status=400)


        test_code =f"{123456}"
        if settings.DEBUG:
            code = test_code
        else:
            code = f"{randbelow(100000):06}"



        otp_entry = EmailOTP.objects.create(email=email, code=code)



        try:
            send_mail(
                subject="Your OTP Code",
                message=f"Your OTP code is: {code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as e :
            otp_entry.delete()

            return Response({"error": f"Failed to send email: {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "OTP code sent to your email"}, status=status.HTTP_200_OK)




class VerifyOTPView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        code = serializer.validated_data.get("code")


        otp = EmailOTP.objects.filter(email=email, code=code).last()
        if otp is None:
            return Response({"error": "Invalid code"}, status=400)


        if otp.is_expired():
            return Response({"error": "OTP code expired"}, status=400)


        user, created = User.objects.get_or_create(
            email=email,
            defaults={"phone_number": f"000000000{randbelow(10)}"}
        )


        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            "message": "OTP verified successfully",
            "access": access_token,
            "refresh": refresh_token
        }, status=200)
