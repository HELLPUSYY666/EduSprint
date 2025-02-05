import os
import django
from rest_framework.test import APITestCase
from django.urls import reverse
from courses.views import *
from datetime import datetime
from courses.models import Course
from users.models import CustomUser

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edusprint.settings")
django.setup()


class CourseListViewTest(APITestCase):
    def test_course_list(self):
        instructor = CustomUser.objects.create_user(username="ZAKA", password="password123")
        course1 = Course.objects.create(title='Django - 1', description='This is the django course',
                                        instructor=instructor,
                                        created_at=datetime.now())
        course2 = Course.objects.create(title='Django - 2', description='This is the second django course',
                                        instructor=instructor,
                                        created_at=datetime.now())
        url = reverse('course-list')
        response = self.client.get(url)
        print(url)
        print(response.status_code)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertEqual(response.status_code, 200)
