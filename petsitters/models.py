from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Member

class petsitters_post(models.Model):

    id = models.AutoField(primary_key=True)
    category = models.CharField(verbose_name='구분', max_length=20, default='' )
    member = models.ForeignKey(to=Member, verbose_name='작성자', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='제목', max_length=200)
    image = models.ImageField(verbose_name='이미지', upload_to='petsitters/images/', null=True, blank=True)
    date_start = models.CharField(verbose_name='임시보호 시작 날짜',max_length=100, null=True)
    date_end = models.CharField(verbose_name='임시보호 종료 날짜',max_length=100, null=True)

    pay = models.IntegerField(verbose_name='임시보호 수수료', default=0)
    address = models.CharField(verbose_name='주소', max_length=200, default='')
    phone_number = models.CharField(verbose_name='연락처',max_length=15,null=True)
    etc = models.CharField(verbose_name='기타사항',max_length=200,null=True)

    view_count = models.IntegerField(verbose_name='조회수', default=0)
    create_time = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

class petsitters_comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(verbose_name='내용', max_length=200)
    post_id = models.ForeignKey(to=petsitters_post, on_delete=models.CASCADE)

class petsitters_apply(models.Model):

    image = models.ImageField(verbose_name='본인사진', upload_to='petsitters/images/', null=True, blank=True)
    name = models.ForeignKey(to=Member,verbose_name='이름', on_delete=models.CASCADE, null=True, blank=True)
    number = models.CharField(verbose_name='연락처', max_length=20, default='')
    family = models.CharField(verbose_name='가구원', max_length=20, default='')
    rnn = models.CharField(verbose_name='주민번호', max_length=20, default='')
    address = models.CharField(verbose_name='주소', max_length=200, default='')
    lisence_hold = models.CharField(verbose_name='자격증 보유여부', max_length=20, default='')
    pet_experience = models.CharField(verbose_name='반려동물 경험', max_length=20, default='')
    pet_species = models.CharField(verbose_name='동물 종류', max_length=20, default='')
    exprience_essay = models.TextField(verbose_name='임보 경험')
    allergy_essay = models.TextField(verbose_name='알레르기 경험')