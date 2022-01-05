from django.contrib.auth import get_user_model
from rest_framework import permissions, response, status
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    UserRefreshTokenSerializer,
)

User = get_user_model()


class UserCreateView(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        refresh = RefreshToken.for_user(user)

        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return response.Response(res, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()


class UserLoginView(TokenObtainPairView):
    permission_classes = []
    serializer_class = UserLoginSerializer


class UserRefreshTokenView(TokenRefreshView):
    serializer_class = UserRefreshTokenSerializer
