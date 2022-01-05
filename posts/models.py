from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    theme = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    picture = models.ImageField(upload_to="post_pictures", null=False, blank=False)
    likes = models.IntegerField(null=True, blank=True, default=0)
    dislikes = models.IntegerField(null=True, blank=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.theme
