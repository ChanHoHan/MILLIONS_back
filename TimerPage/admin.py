from django.contrib.admin import AdminSite
from django.contrib import admin

# Register your models here.
from .models import Timer


class TimerAdmin(AdminSite):
    site_header = "TimerPage"
    site_title = "This is TimerPage"
    index_title = "TimerPage"

Tm_admin_site = TimerAdmin(name="Tm_admin")
Tm_admin_site.register(Timer)
