from django.db import models
from customers.models import Member
from django.contrib.auth import get_user_model

from accounts.models import Member

class board_post(models.Model):
    CATEGORY_CHOICES =[
        ('1', '질문'),
        ('2', '소통'),
        ('3', '정보'),
        ('4', '일상'),
    ]

    id = models.AutoField( primary_key=True)
    title = models.CharField(verbose_name='제목', max_length=200)
    content = models.TextField(verbose_name='내용')
    category = models.CharField(verbose_name='카테고리', max_length=1, choices=CATEGORY_CHOICES, default='1' )
    nickname = models.ForeignKey(to=Member, on_delete = models.CASCADE,null=True, blank=True)
    file = models.FileField(verbose_name='첨부파일',upload_to='posts/uploads/', null=True, blank=True)
    
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    create_time = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

class board_comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(verbose_name='내용', max_length=200)
    post_id = models.ForeignKey(to=board_post, on_delete = models.CASCADE)