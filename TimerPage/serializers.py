from TimerPage.models import Timer
from rest_framework import serializers


class TimerSerializer(serializers.ModelSerializer):
    timerOwner = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Timer
        fields = ('pk', 'timerOwner', 'category', 'hour',
                  'minute', 'second', 'is_main_category')
