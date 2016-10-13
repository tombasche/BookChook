from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Book(models.Model):
    name = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.name
