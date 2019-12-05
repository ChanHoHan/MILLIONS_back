from UserManage.models import User # Login model에서 가져오기
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = User
        fields=['user_id', 'password', 'email', 'desc', 'author'] #fields = '__all__'

