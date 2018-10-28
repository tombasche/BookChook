from __future__ import unicode_literals

from django.db import models


class Series(models.Model):
    """
    Defines a series. A series can have many books
    """
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200, default="admin")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Defines the model for a book object
    """
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    user = models.CharField(max_length=200, default="admin")

    STATUSES = (
        ('current', 'Current'),
        ('archived', 'Removed'),
    )
    status = models.CharField(max_length=20, choices=STATUSES, default="current")
    series = models.ForeignKey(Series, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField(null=True, blank=True)
    tags = models.CharField(max_length=2000, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    comment = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name
