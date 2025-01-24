from django.db import models
from users.models import CustomUser


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='instructed_courses')
    created_at = models.DateTimeField(auto_now_add=True)


class Lesson(models.Model):
