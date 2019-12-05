from django.shortcuts import render
from rest_framework import viewsets
from UserManage.models import User
from UserManage.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all() # User 모델을 기반으로 쿼리셋 생성
    authentication_classes = ['BasicAuthentication', 'SessionAuthentication']
    serializer_class = UserSerializer # serializer 클래스

    """def get_queryset(self):
        qs = super().get_queryset() # 현재 객체의 부모
        # filter
        # qs = qs.filter(author=4) // 요런식으로
        #!!! 지금 만약 로그인이 되어있다면, 활성화된 유저 queryset 필터링, or 로그인 X, querset X !!!
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user) # 현재 활성화된 유저만 queryset 필터링!!
        else:
            qs = qs.none()
            
        #return super().get_queryset()
        return qs

    def perform_create(self, serializer):
         serializer.save(author=self.request.user)
    """

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    # 현재 request를 보낸 유저
    # == self.request.user

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user)
        else:
            qs = qs.none()
        return qs
