from django.shortcuts import render
from rest_framework import viewsets
from LoginPage.models import Login
from LoginPage.serializers import LoginSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
