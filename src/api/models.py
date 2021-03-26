from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager


class AbstractModel(models.Model):
    """
    Abstract model for Song and Podcast as they share some of the fields
    """

    name = models.CharField(max_length=100, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    upload_time = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Song(AbstractModel):
    pass

class Podcast(AbstractModel):

    host = models.CharField(max_length=100, blank=False, null=False)
    participants = TaggableManager()
    # Using tags field to store list of strings


class Audiobook(models.Model):
    """
    Audiobook does not inherit from AbstractModel as the required fields are a bit different
    """

    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    narrator = models.CharField(max_length=100, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    upload_time = models.DateTimeField(default=timezone.now)
