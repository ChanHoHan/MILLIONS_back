from django.contrib import admin
from django.urls import path, include
import LoginPage.urls
import SignUpPage.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('LoginPage.urls')),
    path('',include('SignUpPage.urls')),
]
