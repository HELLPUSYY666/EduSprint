from django.db import models
from users.models import CustomUser
from courses.models import Course


class Certificate(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='certificates')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates')
    issued_at = models.DateTimeField(auto_now_add=True)
