from django.core.mail import send_mail


def send_welcome_email(user_email):
    send_mail(
        'Вы подписались на рассылку'
        'Мы будем присылать вам много спама'
        [user_email],
        fail_silently=False
    )
