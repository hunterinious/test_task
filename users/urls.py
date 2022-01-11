from django.urls import path
from .views import (
    UserCreateView,
    UserLoginView,
    UserRefreshTokenView,
    UserAcitvityView,
)


urlpatterns = [
    path('create', UserCreateView.as_view(), name='api-user-create'),
    path('login', UserLoginView.as_view(), name='api-user-login'),
    path('refresh', UserRefreshTokenView.as_view(), name='api-refresh-token'),
    path('<int:pk>/activity', UserAcitvityView.as_view(), name='api-user-activity')
]