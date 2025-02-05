import os
import django
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from courses.views import *
from datetime import datetime
from courses.models import Course
from users.models import CustomUser
from courses.serializer import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edusprint.settings")
django.setup()


class CourseListViewTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="ZAKA", password="password123")
        self.client.login(username='ZAKA', password='password123')
        self.url = reverse('course-list')

        self.course1 = Course.objects.create(
            title='Django - 1',
            description='This is the django course',
            instructor=self.user,
            created_at=datetime.now()
        )
        self.course2 = Course.objects.create(
            title='Django - 2',
            description='This is the second django course',
            instructor=self.user,
            created_at=datetime.now()
        )

    def test_course_list(self):
        response = self.client.get(self.url)

        serializer_data = CourseSerializer([self.course1, self.course2], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)


class CourseDetailViewTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="ZAKA", password="password123")
        self.client.login(username='ZAKA', password='password123')
        self.course = Course.objects.create(title='Django - 1', description='Django course', instructor=self.user)

    def test_course_detail_view(self):
        response = self.client.get(reverse('course-detail', kwargs={'pk': self.course.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django - 1')
        self.assertContains(response, 'Django course')


class CourseCreateViewTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="ZAKA", password="password123")
        self.client.login(username='ZAKA', password='password123')

    def test_course_create_view(self):
        data = {
            'title': 'Django - 1',
            'description': 'Django course',
            'instructor': self.user.id
        }
        response = self.client.post(reverse('course-create'), data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Course.objects.count(), 1)
        course = Course.objects.first()
        self.assertEqual(course.title, 'Django - 1')
        self.assertEqual(course.description, 'Django course')


class CourseUpdateViewTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="ZAKA", password="password123")
        self.client.login(username='ZAKA', password='password123')
        self.course = Course.objects.create(title='Django - 1', description='Django course', instructor=self.user)

    def test_course_update_view(self):
        data = {'title': 'Updated Django - 1', 'description': 'Updated description', 'instructor': self.user.id}
        response = self.client.post(reverse('course-update', kwargs={'pk': self.course.pk}), data)
        self.assertEqual(response.status_code, 302)
        self.course.refresh_from_db()
        self.assertEqual(self.course.title, 'Updated Django - 1')


class CourseDeleteViewTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="ZAKA", password="password123")
        self.client.login(username='ZAKA', password='password123')
        self.course = Course.objects.create(title='Django - 1', description='Django course', instructor=self.user)

    def test_course_delete_view(self):
        response = self.client.post(reverse('course-delete', kwargs={'pk': self.course.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Course.objects.count(), 0)


class LessonListViewTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="ZAKA", password="password123")
        self.client.login(username='ZAKA', password='password123')

        self.course1 = Course.objects.create(
            title='Django - 1',
            description='This is the django course',
            instructor=self.user,
            created_at=datetime.now()
        )
        self.lesson1 = Lesson.objects.create(
            course=self.course1,
            title='THIS IS THE FIRST LESSON',
            video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            content='Content of this lesson'
        )

    def test_lesson_list_view(self):
        url = reverse('lesson-list')
        response = self.client.get(url)

        serializer_data = LessonSerializer([self.lesson1], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)
