# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import operate_time
from django.utils import timezone
import time


@shared_task
def celery():
    click_command = "celery"
    click_time = timezone.now()
    done_time = timezone.now()
    time_gap = done_time - click_time
    form_new = operate_time(click_time=click_time, done_time=done_time, time_gap=time_gap, click_command=click_command)
    form_new.save()

@shared_task
def celery_delay():
    click_command = "celery_delay"
    click_time = timezone.now()
    time.sleep(10)
    done_time = timezone.now()
    time_gap = done_time - click_time
    form_new = operate_time(click_time=click_time, done_time=done_time, time_gap=time_gap, click_command=click_command)
    form_new.save()