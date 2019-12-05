from django.db import models
from django.conf import settings


class Timer(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    hour = models.CharField(max_length=30, default="0")
    minute = models.CharField(max_length=2, default="0")
    second = models.CharField(max_length=2, default="0")
    is_main_category = models.BooleanField()
