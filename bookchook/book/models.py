from __future__ import unicode_literals

from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200, default="admin")

    def __str__(self):
        return self.name


class Book(models.Model):

    isbn = models.CharField(max_length=13, null=True, blank=True)
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

    location = models.CharField(max_length=500, null=True, blank=True)
    comment = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name


class ISBNBook(models.Model):

    isbn = models.CharField(max_length=13, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    user = models.CharField(max_length=200, default="admin", null=True, blank=True)

    STATUSES = (
        ('current', 'Current'),
        ('archived', 'Removed'),
    )
    status = models.CharField(max_length=20, choices=STATUSES, default="current")
    series = models.ForeignKey(Series, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField(null=True, blank=True)

    location = models.CharField(max_length=500, null=True, blank=True)
    comment = models.CharField(max_length=2000, null=True, blank=True)
