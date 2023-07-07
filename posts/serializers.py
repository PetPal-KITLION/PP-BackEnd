from rest_framework.serializers import  ModelSerializer
from .models import board_post, board_comment
from accounts.models import Member
from rest_framework import serializers


class ExportMemberNicknameSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ['nickname']
class BoardPostBaseSerializer(ModelSerializer):
    class Meta:
        model = board_post
        fields = '__all__'

class BoardPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = board_post
        fields = '__all__' 

class BoardCommentSerializer(ModelSerializer):
    class Meta:
        model = board_comment
        fields = '__all__'
