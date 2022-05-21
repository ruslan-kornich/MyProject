from django.core.mail import send_mail


def send(user_email):
    send_mail('Вы подписались на рассылку',
              "Mы будем присылать вам много ненужного спама",
              'free-protect@ukr.net',
              [user_email],
              fail_silently=False,
              )
