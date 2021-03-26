from .viewsets import AudioBookViewSet, SongViewSet, PodcastViewSet
from rest_framework import routers

'''
django-rest-framework's router generates urlpatterns automatically based on the viewset
'''

router = routers.DefaultRouter()
router.register('song', SongViewSet, basename="song")
router.register('podcast', PodcastViewSet, basename="podcast")
router.register('audiobook', AudioBookViewSet, basename="audiobook")
