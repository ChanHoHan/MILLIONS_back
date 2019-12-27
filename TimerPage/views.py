from django.shortcuts import render
from TimerPage.models import Timer
from TimerPage.serializers import TimerSerializer
from rest_framework import viewsets

class TimerViewSet(viewsets.ModelViewSet):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(user = self.request.user)
        else:
            qs = qs.none()
        return qs
