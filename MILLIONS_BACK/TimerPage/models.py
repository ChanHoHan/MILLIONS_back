from django.db import models
from django.conf import settings
#from UserManage.models import User
#from django.contrib.auth.models import User

class Timer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1,on_delete = models.CASCADE)
    category = models.CharField(max_length=30)
    hour = models.CharField(max_length=30, default="0")
    minute = models.CharField(max_length=2, default="0")
    second = models.CharField(max_length=2, default="0")
    is_main_category = models.BooleanField()
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1,on_delete=models.CASCADE)
