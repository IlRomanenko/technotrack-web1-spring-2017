from django.db import models

from webapp import settings


# Create your models here.


class Category(models.Model):
    type = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.type


class Blog(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(verbose_name="Описание")

    categories = models.ManyToManyField(Category)

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    creation_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title


class Post(models.Model):
    name = models.CharField(max_length=1000)
    content = models.TextField()

    blog = models.ForeignKey(Blog)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    creation_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('creation_time',)

    def __str__(self):
        return self.name
