from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class PostManager(models.Manager):
    def get_all(self):
        return self.objects.all()


class Post(models.Model):
    theme = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    picture = models.ImageField(upload_to="post_pictures", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    objects = PostManager()

    def __str__(self):
        return self.theme


class PostLikeBaseManager(models.Manager):
    def is_exists(self, author_id, post_id):
        return self.filter(author=author_id, post=post_id).exists()

    def get_by_author_and_post_id(self, author_id, post_id):
        queryset = self.filter(author=author_id, post=post_id)
        if queryset:
            return queryset[0]
        return

    def delete_by_id(self, id):
        queryset = self.filter(id=id)
        if queryset:
            queryset[0].delete()
            return True
        return


class PostLikeManager(PostLikeBaseManager):
    pass


class PostDislikeManager(PostLikeBaseManager):
    pass


class PostLike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')

    objects = PostLikeManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'post'], name='user can not like the post twice')
        ]


class PostDislike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_dislikes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_dislikes')

    objects = PostDislikeManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'post'], name='user can not dislike the post twice')
        ]
