from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Series(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200, default="admin")

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    user = models.CharField(max_length=200, default="admin")

    STATUSES = (
        ('current', 'Current'),
        ('archived', 'Removed'),
    )
    status = models.CharField(max_length=20, choices=STATUSES, default="current")
    series = models.ForeignKey(Series, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    tags = TaggableManager()
    location = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
