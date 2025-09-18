from rest_framework import serializers
from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "gender", "email"]



class RequestOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email")


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email", required=True, allow_blank=False)
    code = serializers.CharField(max_length=6, label="Code", required=True, allow_blank=False)

class RequestOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email")