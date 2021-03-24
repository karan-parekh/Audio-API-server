from .viewsets import AudioBookViewSet, SongViewSet, PodcastViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('song', SongViewSet, basename="song")
router.register('podcast', PodcastViewSet, basename="podcast")
router.register('audiobook', AudioBookViewSet, basename="audiobook")
