#from rest_framework.response import Response
from rest_framework import viewsets
from .models import board_post, board_comment
from .serializers import BoardPostSerializer, BoardCommentSerializer

class BoardPostViewSet(viewsets.ModelViewSet):
    queryset = board_post.objects.all()
    serializer_class = BoardPostSerializer

class BoardCommentViewSet(viewsets.ModelViewSet):
    queryset = board_comment.objects.all()
    serializer_class = BoardCommentSerializer
