import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

app = Celery('rest')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery beat tasks
app.conf.beat_schedule = {
    'send-spam-every-5-minute': {
        'task': 'main.tasks.send_beat_email',
        'schedule': crontab(minute='*/5')
    },
}
