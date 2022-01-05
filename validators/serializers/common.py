from rest_framework import serializers
from django.core import exceptions
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validators

User = get_user_model()


def validate_password(data):
    password = data.get('password')
    user = User(data['email'], password)

    errors = dict()

    try:
        if password:
            validators.validate_password(password=password, user=user)
    except exceptions.ValidationError as e:
        errors['password'] = list(e.messages)

    if errors:
        raise serializers.ValidationError(errors)

    return data
