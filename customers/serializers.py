from enum import member
from rest_framework import serializers
from .models import Customers, Customers_comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_customers_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Member

class Customer_PostSerializer():
    class PostPost(member,serializers.ModelSerializer):
        class Meta:
            model = Customers
            fields = ['title','content',member,'category']
    class PostGet(serializers.ModelSerializer):
        class Meta:
            model=Customers
            fields = ['title','content','likes','comment','memberId','category']
    class CommentPost(member,serializers.ModelSerializer):
        class Meta:
            model=Customers_comment
            fields = ['content','postId',member]
    class CommentLikePost(member,serializers.ModelSerializer):
        class Meta:
            model=Customers_comment
            fields=['id','postId',member]
    class ChatPost(serializers.ModelSerializer):
        class Meta:
            model=Customers_comment
            fields=['postId']
    class CommentToCommentPost(serializers.ModelSerializer):
        class Meta:
            model=Customers_comment
            fields=['id','content']
    class CommentGet(serializers.ModelSerializer):
        class Meta:
            model=Customers_comment
            fields=['id']

