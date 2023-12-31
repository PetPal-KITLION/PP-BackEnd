from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from .models import board_post, board_comment
from .serializers import BoardPostBaseSerializer, BoardPostListSerializer, BoardCommentSerializer, ExportMemberNicknameSerializer

from accounts.models import Member
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

# Board - Create
class BoardPostCreateView(APIView):
    def post(self,request):
        token = self.request.headers.get('Authorization')
        if token:
            try:
                user = Member.objects.get(token=token)
                serializer = BoardPostBaseSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(nickname=user)
                    return Response({'data':serializer.data,'nickname':user.nickname})
            except ObjectDoesNotExist:
                Response({'error':'토큰유효 x'},status=400)
        return Response({'error':'로그인하셈'},status=401)
    

# Board - Retrieve        
class BoardPostBaseViewSet(viewsets.ModelViewSet):
    queryset = board_post.objects.all()
    serializer_class = BoardPostBaseSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BoardPostListSerializer
        return super().get_serializer_class()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        post = get_object_or_404(board_post, pk=pk)
        serializer = self.get_serializer(post)
        return Response(serializer.data)
    
    '''def create_comment(self, request, pk=None):
        token = self.request.headers.get('Authorization')
            user = Member.objects.get(token=token)
            if token:
                serializer.save(nickname=user)
                return Response({'message':'글이 등록되었습니다.'})
            return Response({'error':'로그인이 필요합니다.'}) 
'''
# Post - Update
class BoardPostUpdateView(generics.UpdateAPIView):
    queryset = board_post.objects.all()
    serializer_class = BoardPostBaseSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({'error':'로그인이 필요합니다.'})

# Board - Delete
class BoardPostDestroyView(generics.DestroyAPIView):
    queryset = board_post.objects.all()
    serializer_class = BoardPostBaseSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            return Response({'message':'글이 삭제되었습니다.'})
        return Response({'error':'로그인이 필요합니다.'})

# Board - Comment
#class BoardCommentViewSet(viewsets.ModelViewSet):
#    queryset = board_comment.objects.all()
#    serializer_class = BoardCommentSerializer
    
