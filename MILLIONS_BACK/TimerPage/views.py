from django.shortcuts import render
from TimerPage.models import Timer
from TimerPage.serializers import TimerSerializer
from rest_framework import viewsets

class TimerViewSet(viewsets.ModelViewSet):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
