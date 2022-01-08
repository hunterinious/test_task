from django.urls import path
from .views import (
    PostCreateView,
    PostCreateLikeView,
    PostCreateDislikeView,
)


urlpatterns = [
    path('create', PostCreateView.as_view(), name='api-post-create'),
    path('likes/create', PostCreateLikeView.as_view(), name='api-post-like-create'),
    path('dislikes/create', PostCreateDislikeView.as_view(), name='api-post-dislike-create'),
]