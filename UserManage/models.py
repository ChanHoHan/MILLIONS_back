from django.db import models

# Login 모델과 SignUp 모델을 User 모델로 병합
# Login과 SignUp에 사용 될 데이터 베이스를 연결해서 Login 페이지와 SignUp 페이지에 뿌려줄 예정
# User 모델에 필요한 필드 ( 추가 예정 )
# : user_id, password, email, is_user ( ForeignKey ), desc,

class User(models.Model):
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    emali = models.CharField(max_length=30, default="abc@abc.abc") # 필드 만들때, default 옵션 추가 해주세요!!!
    #is_user = models.ForeignKey() // ForeignKey는 데이터 베이스에서 Many to One 관계
    desc = models.TextField(max_length=100, default="default description")
    
""" 유저 정보들을 받으면 json형태의 파일로 저장되며, serializer에 의해서 API 통신 (By Axios Library) 이 될 예정. """

""" 
    ** 구현 List **
    1. Login, SignUp 구성
    2. Login, SignUp 보안관련 (Django 내장 Library 활용, or Base64 보안 관련 기술 구현)
    3. Axios를 통해 Page와 직접 연결

"""