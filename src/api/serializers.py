from rest_framework import serializers
from .models import Audiobook, Song, Podcast
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = "__all__"


class PodcastSerializer(TaggitSerializer, serializers.ModelSerializer):

    participants = TagListSerializerField()

    class Meta:
        model = Podcast
        fields = "__all__"

    def create(self, validated_data):
        participants = validated_data.pop("participants")

        for participant in participants:
            if len(participant) > 100:
                raise  serializers.ValidationError(
                    {"particpants", "Participant name cannot be more than 100 characters"}
                )

        participants = list(map(lambda p: p.lower(), participants))
        podcast = Podcast.objects.create(**validated_data)
        podcast.save()
        podcast.participants.set(*participants)

        return podcast


class AudioBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audiobook
        fields = "__all__"
