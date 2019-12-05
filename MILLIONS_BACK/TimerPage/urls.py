from rest_framework.routers import DefaultRouter
from django.urls import path, include
from TimerPage import views

router = DefaultRouter()
router.register('timer', views.TimerViewSet)

print("MILLIONS_timer")

urlpatterns = [
    path('', include(router.urls)),
]