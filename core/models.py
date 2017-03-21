from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    attached_file = models.FileField(blank=True, null=True)
