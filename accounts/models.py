from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model

class MemberManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)

class Member(AbstractBaseUser):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(verbose_name='이름', max_length=100, default='')
    email = models.EmailField(verbose_name='이메일', unique=True)
    nickname = models.CharField(verbose_name='닉네임', max_length=100)
    password = models.CharField(verbose_name='비밀번호', max_length=128)
    phone = models.CharField(verbose_name='전화번호', max_length=20, default = '')
    address = models.CharField(verbose_name="주소", max_length=100, default = '')
    age = models.IntegerField(verbose_name="나이", default=0)
    
    token = models.TextField(verbose_name='토큰', default='')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Pet(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(verbose_name='펫이름', max_length=100)
    species = models.CharField(verbose_name='종', max_length=100)
    age = models.IntegerField(verbose_name='펫나이')
    feature = models.TextField(verbose_name='펫특이사항')
    member = models.ForeignKey(to=Member, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return self.pet_name
    
class Review(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    content = models.TextField(verbose_name='리뷰내용', default='')
    score = models.IntegerField(verbose_name='점수')
    reviewer = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='given_reviews', default = '')
    receiver = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='received_reviews', default = '')
    
    def __str__(self):
        return f"Review {self.score}"