from django.contrib import admin
from django.urls import path, include
from TimerPage import urls
from rest_framework import urls
from django.conf import settings
#from django.conf.urls.static import static

print("MILLIONS_BACK")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TimerPage.urls')),
    path('api-auth/', include('rest_framework.urls')),
]