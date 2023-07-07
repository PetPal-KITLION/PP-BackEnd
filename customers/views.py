from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_Customers_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages

from accounts import serializers

from .serializers import Customer_PostSerializer
from .models import Customers,Customers_comment

class Community_Write(APIView):
    def post(self, request):
        if(request.method=='POST'):
            serializer = Customer_PostSerializer.PostPost(self,data = request.POST)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'글 작성 완료'})
            return Response(serializer.errors, status =  400)
class Community_Read(APIView):
   def get(request):
        if(request.method=='GET'):
            serializer = Customer_PostSerializer.GetPost(data = request.GET)
            category=serializer.data.get("category")
            Post=get_Customers_model
        try:
            posts= Post.objects.filter(category).all
            return Response({'category': category}, status=200)
        except Post.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
class Community_Comment_Write(APIView):
    def post(self,request):
         if(request.method=='POST'):
            serializer = Customer_PostSerializer.CommentPost(self,data = request.POST)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'댓글 작성 완료'})
            return Response(serializer.errors, status =  400)
class Community_Comment_Like_Write(APIView):
    def post(self,request):
        if(request.method=='POST'):
            serializer=Customer_PostSerializer.CommentLikePost(self,date=request.POST)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'댓글 좋아요 완료'})
            return Response(serializer.errors, status =  400)
class Community_CommentToComment_Write(APIView):
    def post(self,request):
        if(request.method=='POST'):
            serializer=Customer_PostSerializer.CommentToCommentPost(self,date=request.POST)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'대댓글 작성 완료'})
            return Response(serializer.errors, status =  400)
class Best_Read(APIView):
   def get(request):
        if(request.method=='GET'):
            serializer = Customer_PostSerializer.Get(data = request.GET)
            Post=Customers.all
        try:
            posts= Post.objects.filter(serializer.viewCount).all
            return Response({'인기순 조회'}, status=200)
        except Post.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
class Comment_Read(APIView):
   def get(request):
        if(request.method=='GET'):
            serializer = Customer_PostSerializer.CommentGet(data = request.GET)
            Comment=Customers_comment.all
            postId=serializer.postId
        try:
            comments= Comment.objects.filter(postId).all
            return Response({'post pk:':postId }, status=200)
        except Comment.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)