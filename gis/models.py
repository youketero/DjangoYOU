from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

text_len = 360


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=2000)
    text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > text_len:
            return self.text[:text_len]
        else:
            return self.text


class point(models.Model):
    title = models.CharField(max_length=20)
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
