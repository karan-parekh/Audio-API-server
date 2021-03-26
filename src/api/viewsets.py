from rest_framework import viewsets
from .models import Audiobook, Podcast, Song

from .serializers import AudioBookSerializer, PodcastSerializer, SongSerializer

'''
Using django-rest-framework's ModelViewSets
ModelViewSet provides built-in actions for different HTTP methods as follows

GET     .list() / .retrieve()
POST    .create()
PUT     .update()
PATCH   .partial_update()
DELETE  .destroy()

These methods can be overwritten for customized behavior
'''

class SongViewSet(viewsets.ModelViewSet):

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PodcastViewSet(viewsets.ModelViewSet):

    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class AudioBookViewSet(viewsets.ModelViewSet):

    queryset = Audiobook.objects.all()
    serializer_class = AudioBookSerializer
