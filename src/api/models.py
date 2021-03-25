from django.db import models
from django.utils import timezone


class AbstractModel(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    upload_time = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Song(AbstractModel):
    pass

class Podcast(AbstractModel):

    host = models.CharField(max_length=100, blank=False, null=False)
    participants = models.CharField(max_length=100, null=True)


class Audiobook(models.Model):

    title = models.CharField(max_length=100, blank=False, null=False, unique=True)
    author = models.CharField(max_length=100, blank=False, null=False)
    narrator = models.CharField(max_length=100, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    upload_time = models.DateTimeField(default=timezone.now)
