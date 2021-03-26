import json

from datetime import datetime

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone

from api.models import Audiobook


class TestAudiobookModel(APITestCase):

    def setUp(self) -> None:
        self.audiobook_url = "/api/audiobook/"
        self.audiobook_data = {
            "title": "Inferno Squad",
            "author": "Christie Golden",
            "narrator": "Janina Gavankar",
            "duration": 32455,
            "upload_time": timezone.now()
        }

        self.audiobook = Audiobook(**self.audiobook_data)
        self.audiobook.save()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_audiobook_create(self):
        response = self.client.post(self.audiobook_url, self.audiobook_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_audiobook_detail_retrieve(self):
        response = self.client.get(reverse("audiobook-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_audiobook_list(self):
        response = self.client.get(self.audiobook_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_audiobook_update(self):
        update_fields = {
            "title": "Lorem Ipsum",
            "author": "Jon Doe",
        }
        response = self.client.patch(reverse("audiobook-detail", kwargs={"pk": 1}), update_fields)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['title'], update_fields['title'])
        self.assertEqual(response_data['author'], update_fields['author'])

    def test_audiobook_delete(self):
        response = self.client.delete(reverse("audiobook-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # NEGATIVE TESTS

    def test_name_len_gt_100(self):
        '''
        Test for name field >100 characters
        Works for any field with max_length constraint
        '''
        data = self.audiobook_data
        data['title'] = "".join(["a" for _ in range(110)])
        response = self.client.post(self.audiobook_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_duration(self):
        data = self.audiobook_data
        data["duration"] = -20
        response = self.client.post(self.audiobook_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_field(self):
        data = self.audiobook_data
        data.pop("title")
        response = self.client.post(self.audiobook_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_upload_time_in_past(self):
        # setting upload_time to yesterday
        now  = timezone.now()
        date = datetime(now.year, now.month, now.day-1)
        data = self.audiobook_data
        data["upload_time"] = date
        
        response = self.client.post(self.audiobook_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
