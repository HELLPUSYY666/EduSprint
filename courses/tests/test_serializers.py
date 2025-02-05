from django.test import TestCase
from courses.models import Course
from courses.serializer import CourseSerializer
from users.models import CustomUser


class TestCourseSerializer(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="ZAKA", password="password123")
        self.client.login(username='ZAKA', password='password123')

    def test_serializer(self):
        self.course1 = Course.objects.create(
            title='Django - 1',
            description='This is the django course',
            instructor=self.user
        )
        self.course2 = Course.objects.create(
            title='Django - 2',
            description='This is the second django course',
            instructor=self.user
        )

        data = CourseSerializer([self.course1, self.course2], many=True).data

        expected_data = [
            {
                'id': self.course1.id,
                'title': 'Django - 1',
                'description': 'This is the django course',
                'instructor': self.user.id,
            },
            {
                'id': self.course2.id,
                'title': 'Django - 2',
                'description': 'This is the second django course',
                'instructor': self.user.id,
            }
        ]

        # Игнорируем 'created_at' в сериализаторе, проверяя только нужные поля
        self.assertEqual(
            [{k: v for k, v in item.items() if k != 'created_at'} for item in data],
            [{k: v for k, v in item.items() if k != 'created_at'} for item in expected_data]
        )

