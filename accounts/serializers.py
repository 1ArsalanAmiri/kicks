from rest_framework import serializers


class RequestOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email")


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email", required=True, allow_blank=False)
    code = serializers.CharField(max_length=6, label="Code", required=True, allow_blank=False)

