from __future__ import unicode_literals

from django.db import models


class Theater(models.Model):
    link = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    address = models.CharField(max_length=225)

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    theater = models.ForeignKey(Theater)
    name = models.CharField(max_length=225)
    image = models.CharField(max_length=600)
    screen_format = models.CharField(max_length=300)
    duration = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name


class Showtime(models.Model):
    movie = models.ForeignKey(Movie)
    book_link = models.CharField(max_length=225, blank=True)
    time = models.TimeField()

    def __unicode__(self):
        return str(self.time)


class Tags(models.Model):
    name = models.CharField(max_length=225)
    movie = models.ManyToManyField(Movie)

    def __unicode__(self):
        return self.name
