from django.shortcuts import render
from rest_framework import viewsets
from UserManage.models import User
from UserManage.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
