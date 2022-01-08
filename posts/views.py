from rest_framework.generics import CreateAPIView
from .serializers import PostCreateSerializer, PostCreateLikeSerializer, PostCreateDislikeSerializer


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer


class PostCreateLikeView(CreateAPIView):
    serializer_class = PostCreateLikeSerializer


class PostCreateDislikeView(CreateAPIView):
    serializer_class = PostCreateDislikeSerializer
