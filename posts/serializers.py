from rest_framework.serializers import  ModelSerializer
from .models import board_post, board_comment

class BoardPostSerializer(ModelSerializer):
    class Meta:
        model = board_post
        fields = '__all__'

class BoardCommentSerializer(ModelSerializer):
    class Meta:
        model = board_comment
        fields = '__all__'
