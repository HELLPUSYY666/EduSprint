import os
import django
from rest_framework.test import APITestCase
from django.urls import reverse
from courses.views import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edusprint.settings")
django.setup()


class CourseListViewTest(APITestCase):
    def test_course_list(self):
        url = reverse('course-list')
        print(url)
        response = self.client.get(url)
        print(response)
