from rest_framework import viewsets
from .models import Audiobook, Podcast, Song

from .serializers import AudioBookSerializer, PodcastSerializer, SongSerializer


class SongViewSet(viewsets.ModelViewSet):

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PodcastViewSet(viewsets.ModelViewSet):

    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class AudioBookViewSet(viewsets.ModelViewSet):

    queryset = Audiobook.objects.all()
    serializer_class = AudioBookSerializer
