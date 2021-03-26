import json

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone

from api.models import Song


class TestSongModel(APITestCase):

    def setUp(self):
        self.song_url = "/api/song/"
        self.song_data = {
            "name": "Waving flag",
            "duration": 256,
            "upload_time": timezone.now()
        }

        self.song = Song(**self.song_data)
        self.song.save()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_song_create(self):
        response = self.client.post(self.song_url, self.song_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_song_detail_retrieve(self):
        response = self.client.get(reverse("song-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_song_list(self):
        response = self.client.get(self.song_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_song_update(self):
        update_field = {"name": "The Ketchup Song"}
        response = self.client.patch(reverse("song-detail", kwargs={"pk": 1}), update_field)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['name'], update_field['name'])

    def test_song_delete(self):
        response = self.client.delete(reverse("song-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
