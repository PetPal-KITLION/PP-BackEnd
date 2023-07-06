from django.db import models
from django.contrib.auth import get_user_model

from customers.models import Member


User = get_user_model()

class petsitters_post(models.Model):
    CATEGORY_CHOICES =[
        ('1', '시터신청'),
        ('2', '시터찾기'),
    ]

    id = models.AutoField(primary_key=True)
    category = models.CharField(verbose_name='시터등급', max_length=1, choices=CATEGORY_CHOICES, default='1' )
    member = models.ForeignKey(to=User, verbose_name='작성자', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='제목', max_length=200)
    image = models.ImageField(verbose_name='이미지', upload_to='petsitters/images/', null=True, blank=True)
    data_start = models.CharField(verbose_name='임시보호 시작 날짜',max_length=100, null=True)
    data_end = models.CharField(verbose_name='임시보호 종료 날짜',max_length=100, null=True)

    pay = models.IntegerField(verbose_name='임시보호 수수료', default=0)
    address = models.CharField(verbose_name='주소', max_length=200, default='')
    phone_number = models.CharField(verbose_name='연락처',max_length=15,null=True)
    etc = models.CharField(verbose_name='기타사항',max_length=200,null=True)

    view_count = models.IntegerField(verbose_name='조회수', default=0)
    create_time = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

class petsitters_comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(verbose_name='내용', max_length=200)
    likes = models.ManyToManyField(Member)
    post_id = models.ForeignKey(to=petsitters_post, on_delete=models.CASCADE)
