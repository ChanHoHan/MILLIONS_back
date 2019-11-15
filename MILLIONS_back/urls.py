from django.contrib import admin
from django.urls import path, include
import LoginPage.urls
from TimerPage import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LoginPage.urls')),
    path('', include('TimerPage.urls')),
]
