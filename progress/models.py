from django.db import models
from users.models import CustomUser
from courses.models import Lesson


class Progress(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progress')
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True, null=True)

