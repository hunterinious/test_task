from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model
from .models import Post, PostLike, PostDislike


User = get_user_model()


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateLikeSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = PostLike
        fields = ('id', 'post',)

    def get_id(self, obj):
        return obj.id

    def validate(self, data):
        request_user = self.context['request'].user
        author_like_id = request_user.id
        post = data['post']

        if post.user.id == author_like_id:
            raise ValidationError("author can't like his own post")

        if PostLike.objects.is_exists(author_like_id, post.id):
            raise ValidationError("you can't like the post twice")

        data['author'] = request_user

        return super(PostCreateLikeSerializer, self).validate(data)

    def create(self, validated_data):
        dislike = PostDislike.objects.get_by_author_and_post_id(validated_data['author'].id, validated_data['post'].id)
        if dislike:
            PostDislike.objects.delete_by_id(dislike.id)

        return super(PostCreateLikeSerializer, self).create(validated_data)


class PostLikeAnaliticsParamsSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    date_from = serializers.DateTimeField()
    date_to = serializers.DateTimeField()


class PostLikeAnaliticsSerilizer(serializers.Serializer):
    post_id = serializers.IntegerField()
    day = serializers.DateTimeField()
    likes_amount = serializers.IntegerField()


class PostCreateDislikeSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = PostDislike
        fields = ('id', 'post',)

    def get_id(self, obj):
        return obj.id

    def validate(self, data):
        request_user = self.context['request'].user
        author_like_id = request_user.id
        post = data['post']

        if post.user.id == author_like_id:
            raise ValidationError("author can't dislike his own post")

        if PostDislike.objects.is_exists(author_like_id, post.id):
            raise ValidationError("you can't dislike the post twice")

        data['author'] = request_user

        return super(PostCreateDislikeSerializer, self).validate(data)

    def create(self, validated_data):
        like = PostLike.objects.get_by_author_and_post_id(validated_data['author'].id, validated_data['post'].id)
        if like:
            PostLike.objects.delete_by_id(like.id)

        return super(PostCreateDislikeSerializer, self).create(validated_data)
