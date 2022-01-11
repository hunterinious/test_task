from rest_framework import serializers
from validators.serializers.common import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
        "input_type": "password"})

    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]

    def validate(self, data):
        data = validate_password(data)
        return super(UserCreateSerializer, self).validate(data)

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_login', 'last_request')
