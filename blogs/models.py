from django.db import models

from webapp import settings

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=1000)
    description = models.TextField(verbose_name="Описание")

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    creation_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title

    pass


class Post(models.Model):

    name = models.CharField(max_length=1000)
    content = models.TextField()

    blog = models.ForeignKey(Blog)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    creation_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    pass
