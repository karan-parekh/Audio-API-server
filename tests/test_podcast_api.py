import json

from datetime import datetime

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone

from api.models import Podcast


class TestPodcastModel(APITestCase):

    def setUp(self):
        self.podcast_url  = "/api/podcast/"
        self.participants = ["Elon Musk", "Jon Doe"]
        self.podcast_data = {
            "name": "Joe Rogan Experience",
            "duration": 5623,
            "upload_time": timezone.now(),
            "host": "Joe Rogan",
        }
        self.podcast = Podcast(**self.podcast_data)
        self.podcast.save()
        self.podcast.participants.set(*self.participants)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_podcast_create(self):
        data = self.podcast_data
        data['participants'] = str(self.participants).replace("'", '"')
        # Replacing {'} with {"} to make the string JSON compatible

        response = self.client.post(self.podcast_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_podcast_detail_retrieve(self):
        response = self.client.get(reverse("podcast-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_podcast_list(self):
        response = self.client.get(self.podcast_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_podcast_update(self):
        update_fields = {
            "name": "Ludicrous Future",
            "host": "Tim Dodd"
        }
        response = self.client.patch(reverse("podcast-detail", kwargs={"pk": 1}), update_fields)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response_data = json.loads(response.content)
        self.assertEqual(response_data['name'], update_fields['name'])
        self.assertEqual(response_data['host'], update_fields['host'])

    def test_podcast_delete(self):
        response = self.client.delete(reverse("podcast-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # NEGATIVE TESTS

    def test_name_len_gt_100(self):
        '''
        Test for name field >100 characters
        Works for any field with max_length constraint
        '''
        data = self.podcast_data
        data['name'] = "".join(["a" for _ in range(110)])
        response = self.client.post(self.podcast_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_duration(self):
        data = self.podcast_data
        data["duration"] = -20
        response = self.client.post(self.podcast_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_field(self):
        data = self.podcast_data
        data.pop("name")
        response = self.client.post(self.podcast_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_participant_name_gt_100(self):
        data = self.podcast_data
        participants = ["".join(["a" for _ in range(110)])]
        data['participants'] = str(participants).replace("'", '"')
        # Replacing {'} with {"} to make the string JSON compatible

        response = self.client.post(self.podcast_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_upload_time_in_past(self):
        # setting upload_time to yesterday
        now  = timezone.now()
        date = datetime(now.year, now.month, now.day-1)
        data = self.podcast_data
        data["upload_time"] = date
        
        response = self.client.post(self.podcast_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



