from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MemberManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class Member(AbstractBaseUser):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(verbose_name='이름', max_length=100, default='')
    email = models.EmailField(verbose_name='이메일', unique=True)
    nickname = models.CharField(verbose_name='닉네임', max_length=100)
    password = models.CharField(verbose_name='비밀번호', max_length=128)
    phone = models.CharField(verbose_name='전화번호', max_length=20, default = '')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'nickname', 'phone']

    def __str__(self):
        return self.email
