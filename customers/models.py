from django.db import models

class Member(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(verbose_name='실명', max_length=20)  # 실명
    password = models.CharField(verbose_name='비밀번호', max_length=30)  # 비밀번호
    nickname = models.CharField(verbose_name='닉네임', max_length=20, unique=True)  # 닉네임
    phone_number = models.CharField(verbose_name='전화번호', max_length=20)  # 전화번호
    email = models.EmailField() # 이메일

class Member_sns(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
# Create your models here.
