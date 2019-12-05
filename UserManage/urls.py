from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from UserManage import views
#from rest_framework.authentication.views import obtain_auth_token

router = DefaultRouter()
router.register('UserManage', views.UserViewSet)

print("MILLIONS_user_manage")

urlpatterns = [
    path('', include(router.urls)),
    #url(r'^api-token-auth/', views.obtain_auth_token),
]