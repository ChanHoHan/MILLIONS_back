from rest_framework.routers import DefaultRouter
from django.urls import path, include
from TimerPage import views
#from TimerPage.admin import Tm_admin_site

router = DefaultRouter()
router.register('timer', views.TimerViewSet)

print("MILLIONS_timer")

urlpatterns = [
    path('', include(router.urls)),
   # path('timer-admin/', Tm_admin_site.urls),
]