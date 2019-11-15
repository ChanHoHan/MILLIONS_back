from django.db import models
from django.conf import settings


class Timer(models.Model):
    timer_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    time = models.CharField(max_length=30, default="00:00:00")
    is_main_category = models.BooleanField()
