# MILLIONS

고려대 세종 멋사7기 밀리언즈 앱 프로젝트 입니다.
밀리언즈는 1만 시간 달성까지 타이머로 본인의 공부시간을 측정하는 앱 입니다.

## 백엔드

   - local 구동
    1. python manage.py runserver 
   - front랑 연결시
    1. python manage.py runserver 0:8000
   
   - 회원가입 페이지 : 0/rest-auth/registration/
   - 유저정보 : 0/admin
   - 타이머 관리 : 0/timer-admin
   - $ pip install -r requirements.txt  <- 해당 명령어로 패키지 다운받아주세요.

## Axios 연결시 Cross-Orgin-Resource-Sharing Issue 해결방법
이러한 이슈(오류)를 해결해주는 패키지가 정의되어 있으므로, 이걸 이용하면 해결됨.

* 먼저 'django-cors-headers' 패키지를 설치
pip install django-cors-headers


* settins.py에 INSTALLED_APPS에 'corsheaders'를 추가
```
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]
```

* settings.py의 MIDDLEWARE에 다음과 같이 추가
```
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```
* 마지막으로 아래 코드도 settings.py에 추가요망 (필수 X)
```
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
```
### ps. (Configuration) 

CORS_ORIGIN_ALLOW_ALL = True\
: WhiteList가 사용되지 않을 것임
\
CORS_ALLOW_METHODS = ['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT', ]\
: CORS을 허용할 HTTP METHOD 지정
\
CORS_ALLOW_CREDENTIALS = True\
쿠키가 HTTP에 저장되어 CORS 전송 
\
> 참고: https://github.com/adamchainz/django-cors-headers
