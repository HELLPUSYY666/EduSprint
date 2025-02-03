from django.core.mail import send_mail
from edusprint.celery import app

from .service import send_welcome_email
from .models import CustomUser


@app.task
def send_welcome_email(user_email):
    send_welcome_email(user_email)
