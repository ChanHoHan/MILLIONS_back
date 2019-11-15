from rest_framework import viewsets
from .models import Timer
from .serializer import TimerSerializer
import logging

logger = logging.getLogger('test')
logger.error('에러')


class TimerViewSet(viewsets.ModelViewSet):
    print(Timer.objects)
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
