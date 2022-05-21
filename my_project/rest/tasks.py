from rest.celery import app
from product.models import Contact
from .service import send
from django.core.mail import send_mail


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail('Вы подписались на рассылку',
            'Мы будем присылать Вам много нежного спама каждые 5 минут',
            'free-protect@ukr.net',
            [contact.email],
            fail_silently=False,
        )
