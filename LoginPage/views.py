from rest_framework import viewsets
from .models import Login
from .serializer import LoginSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer