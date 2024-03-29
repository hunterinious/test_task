from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def set_last_request(self, user):
        user.last_request = timezone.now()
        user.save()

    def get_all(self):
        return self.all()


class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=60, unique=True)
    is_superuser = models.BooleanField(default=False)
    last_request = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()

    def __str__(self):
        return self.email
