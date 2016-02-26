from __future__ import unicode_literals

from django.db import models
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post)
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=20)

    def __unicode__(self):
        return self.text
