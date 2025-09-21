from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RequestOTPSerializer, VerifyOTPSerializer, RegisterUserSerializer
from .models import EmailOTP, User
from django.core.mail import send_mail
from django.conf import settings
from secrets import randbelow
from django.utils import timezone
from datetime import timedelta


class RegisterUserView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]

        last_otp = EmailOTP.objects.filter(email=email).last()
        if last_otp and last_otp.is_blocked():
            remaining = int((last_otp.blocked_until - timezone.now()).total_seconds())
            return Response({"error": f"Too many attempts. Try again in {remaining} seconds."},
                            status=429)

        if last_otp and timezone.now() - last_otp.created_at < timedelta(minutes=2):
            return Response({"error": "You can request OTP once every 2 minutes."},
                            status=429)


        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "first_name": serializer.validated_data["first_name"],
                "last_name": serializer.validated_data["last_name"],
                "gender": serializer.validated_data["gender"],
                "is_active": False
            }
        )

        if settings.DEBUG:
            code = "123456"
        else:
            code = f"{randbelow(1000000):06}"


        otp_entry = EmailOTP.objects.create(email=email, code=code)

        try:
            send_mail(
                subject="Your OTP Code",
                message=f"Your OTP code is: {code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
            )
        except Exception as e:
            otp_entry.delete()
            return Response({"error": f"Failed to send email: {str(e)}"}, status=500)

        return Response({"message": "OTP sent to your email"}, status=200)


class VerifyUserOTPView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        code = serializer.validated_data["code"]

        otp = EmailOTP.objects.filter(email=email, is_used=False).last()
        if not otp:
            return Response({"error": "OTP not found"}, status=400)

        if otp.is_blocked():
            remaining = int((otp.blocked_until - timezone.now()).total_seconds())
            return Response({"error": f"Too many wrong attempts. Try again in {remaining} seconds."}, status=429)

        if otp.is_expired():
            return Response({"error": "OTP expired"}, status=400)

        if otp.code != code:
            otp.attempts += 1
            if otp.attempts >= 5:
                otp.blocked_until = timezone.now() + timedelta(minutes=15)
            otp.save()
            return Response({"error": "Invalid OTP"}, status=400)

        otp.is_used = True
        otp.save()

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({"error": "User not found, please register first."}, status=404)

        user.is_active = True
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })



class RequestOTPView(generics.GenericAPIView):
    serializer_class = RequestOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]


        last_otp = EmailOTP.objects.filter(email=email).last()
        if last_otp:
            if last_otp.is_blocked():
                remaining = int((last_otp.blocked_until - timezone.now()).total_seconds())
                return Response(
                    {"error": f"Too many attempts. Try again in {remaining} seconds."},
                    status=429
                )
            if timezone.now() - last_otp.created_at < timedelta(minutes=2):
                return Response(
                    {"error": "You can request OTP once every 2 minutes."},
                    status=429
                )


        code = "123456" if settings.DEBUG else f"{randbelow(1000000):06}"

        otp_entry = EmailOTP.objects.create(email=email, code=code)

        try:
            send_mail(
                subject="Your OTP Code",
                message=f"Your OTP code is: {code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
            )
        except Exception as e:
            otp_entry.delete()
            return Response({"error": f"Failed to send email: {str(e)}"}, status=500)

        return Response({"message": "OTP sent to your email"}, status=200)
