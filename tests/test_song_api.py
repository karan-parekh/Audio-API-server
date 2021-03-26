import json

from datetime import datetime

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

    # NEGATIVE TESTS

    def test_name_len_gt_100(self):
        '''
        Test for name field >100 characters
        Works for any field with max_length=100 constraint
        '''
        data = self.song_data
        data['name'] = "".join(["a" for _ in range(110)])
        response = self.client.post(self.song_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_duration(self):
        data = self.song_data
        data["duration"] = -20
        response = self.client.post(self.song_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_field(self):
        data = self.song_data
        data.pop("name")
        response = self.client.post(self.song_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_upload_time_in_past(self):
        # setting upload_time to yesterday
        now  = timezone.now()
        date = datetime(now.year, now.month, now.day-1)
        data = self.song_data
        data["upload_time"] = date
        
        response = self.client.post(self.song_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
