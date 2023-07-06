from django.db import models
from django.contrib.auth import get_user_model

from customers.models import Member

User = get_user_model()

class petsitters_post(models.Model):
    CATEGORY_CHOICES =[
        ('1', '일반'),
        ('2', '프리미엄'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='제목', max_length=200)
    content = models.CharField(verbose_name='내용',max_length=200)
    
    #comment는 없어도 될 것 같다.
    comment = models.TextField(verbose_name='댓글',null=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    category = models.CharField(verbose_name='카테고리', max_length=1, choices=CATEGORY_CHOICES, default='1' )
    image = models.ImageField(verbose_name='이미지', upload_to='petsitters/images/', null=True, blank=True)

    member = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    create_time = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

class petsitters_comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(verbose_name='내용', max_length=200)
    likes = models.ManyToManyField(Member)
    post_id = models.ForeignKey(to=petsitters_post, on_delete=models.CASCADE)
