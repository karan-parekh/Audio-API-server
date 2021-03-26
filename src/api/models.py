from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager
from .validators import datetime_validator, duration_validator


class AbstractModel(models.Model):
    """
    Abstract model for Song and Podcast as they share some of the fields
    """

    name = models.CharField(max_length=100, blank=False, null=False)
    duration = models.PositiveIntegerField(blank=False, null=False, validators=[duration_validator])
    upload_time = models.DateTimeField(default=timezone.now, validators=[datetime_validator])

    class Meta:
        abstract = True


class Song(AbstractModel):
    pass

class Podcast(AbstractModel):

    host = models.CharField(max_length=100, blank=False, null=False)
    participants = TaggableManager()
    # Using tags field to store list of strings


class Audiobook(AbstractModel):

    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    narrator = models.CharField(max_length=100, blank=False, null=False)

    name = None  # Setting name field to none as this model has no "name" field
