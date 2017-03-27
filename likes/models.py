from django.db import models

from webapp import settings


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    creation_time = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('blogs.Post')

    pass
