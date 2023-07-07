from django.db import models
from accounts import Member

class Customers(models.Model):
    id = models.AutoField(primary_key=True, unique=True,null=False)
    title = models.CharField(verbose_name='제목', max_length=50,null=False)
    content = models.CharField(verbose_name='내용',null=False)
    comment = models.CharField(verbose_name='댓글', max_length=100,null=True)
    likes= models.manytomanyField(verbose_name='좋아요')
    memberId =  models.ForeignKey(Member, on_delete=models.CASCADE)
    viewCount = models.IntegerField(verbose_name='조회수',null=False)
    createTime = models.DateTimeField(verbose_name="생성시간",auto_now_add=True)
    category=models.CharField(verbose_name="카테고리",null=False)
class Customers_comment(models.Model):
    id=models.AutoField(primary_key=True,unique=True,null=False)
    content=models.CharField(verbose_name='댓글 내용',null=False)
    likes=models.manytomanyField(verbose_name='좋아요')
    postId=models.ForeignKey(Customers,on_delete=models.CASCADE)
