from django.db.models import fields
from rest_framework import serializers
from .models import Audiobook, Song, Podcast


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = "__all__"


class PodcastSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast
        fields = "__all__"


class AudioBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audiobook
        fields = "__all__"
