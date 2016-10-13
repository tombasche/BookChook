from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    user = models.CharField(max_length=200, default="admin")

    def __str__(self):
        return self.name
