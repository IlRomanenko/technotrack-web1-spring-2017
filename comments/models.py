from django.db import models
from webapp import settings


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    post = models.ForeignKey('blogs.Post')

    pass
