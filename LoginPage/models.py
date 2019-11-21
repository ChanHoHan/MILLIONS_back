from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    emali = models.CharField(max_length=30, default="abc@abc.abc")