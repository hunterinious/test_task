from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    PostCreateSerializer,
    PostCreateLikeSerializer,
    PostLikeAnaliticsParamsSerializer,
    PostLikeAnaliticsSerilizer,
    PostCreateDislikeSerializer
)
from .models import PostLike


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer


class PostCreateLikeView(CreateAPIView):
    serializer_class = PostCreateLikeSerializer


class PostCreateDislikeView(CreateAPIView):
    serializer_class = PostCreateDislikeSerializer


class PostLikeGetAnaliticsView(APIView):
    def get(self, request):
        serializer = PostLikeAnaliticsParamsSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        analytic_data = PostLikeAnaliticsSerilizer(
            PostLike.objects.filter_by_period(data['date_from'], data['date_to'], data['post_id']), many=True).data

        return Response(analytic_data, content_type='json')
