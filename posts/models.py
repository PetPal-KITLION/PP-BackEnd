from django.db import models
from customers.models import Member
from django.contrib.auth import get_user_model

User = get_user_model()

class board_post(models.Model):
    CATEGORY_CHOICES =[
        ('1', '질문'),
        ('2', '소통'),
        ('3', '정보'),
        ('4', '일상'),
    ]

    id = models.AutoField(verbose_name='작성자', primary_key=True)
    title = models.CharField(verbose_name='제목', max_length=200)
    content = models.TextField(verbose_name='내용')
    category = models.CharField(verbose_name='카테고리', max_length=1, choices=CATEGORY_CHOICES, default='1' )

    likes = models.ManyToManyField(Member)  
    member_id = models.ForeignKey(to=User, on_delete = models.CASCADE)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    create_time = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

class board_comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(verbose_name='내용', max_length=200)
    likes = models.ManyToManyField(Member)
    post_id = models.ForeignKey(to=User, on_delete = models.CASCADE)