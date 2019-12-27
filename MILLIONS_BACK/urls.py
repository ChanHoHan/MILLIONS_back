from django.contrib import admin
from django.urls import path, include
from TimerPage import urls
from rest_framework import urls
from django.conf import settings
from django.conf.urls import url
#from django.conf.urls.static import static

print("MILLIONS_BACK")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TimerPage.urls')),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')), # 로그인 구현을 위함
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')) #회원가입
]