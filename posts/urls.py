from django.urls import path
from .views import (
    PostCreateView,
    PostCreateLikeView,
    PostLikeGetAnaliticsView,
    PostCreateDislikeView,
)


urlpatterns = [
    path('create', PostCreateView.as_view(), name='api-post-create'),
    path('likes/create', PostCreateLikeView.as_view(), name='api-post-like-create'),
    path('likes/analitics', PostLikeGetAnaliticsView.as_view(), name='api-post-like-get-analitics'),
    path('dislikes/create', PostCreateDislikeView.as_view(), name='api-post-dislike-create'),
]