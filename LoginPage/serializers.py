from UserManage.models import Login # Login model에서 가져오기
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'