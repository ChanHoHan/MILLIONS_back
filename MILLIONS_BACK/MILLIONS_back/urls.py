from django.contrib import admin
from django.urls import path, include
from TimerPage import urls
from LoginPage import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timer/', include('TimerPage.urls')),
    path('login/', include('LoginPage.urls')),
]
