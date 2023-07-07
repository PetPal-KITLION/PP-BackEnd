from rest_framework import viewsets, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Member

from .models import petsitters_post, petsitters_comment, petsitters_apply
from .serializers import PetsittersPostBaseSerializer, PetsittersPostListSerializer, PetsittersCommentSerializer, PetsittersApplyBaseSerializer, PetsittersApplyListSerializer

from django.shortcuts import get_object_or_404

# Post - Create

class PetsittersPostCreateView(APIView):
    def post(self,request):
        token = self.request.headers.get('Authorization')
        if token:
            try:
                user = Member.objects.get(token=token)
                serializer = PetsittersPostBaseSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(member=user)
                    return Response({'data':serializer.data,'nickname':user.nickname})
            except ObjectDoesNotExist:
                Response({'error':'토큰유효 x'},status=400)
        return Response({'error':'로그인하셈'},status=401)

# Post - Retrieve        
class PetsittersPostViewSet(viewsets.ModelViewSet):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PetsittersPostListSerializer
        return super().get_serializer_class()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        post = get_object_or_404(petsitters_post, pk=pk)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def create_comment(self, request, pk=None):
        # 댓글 작성 로직 구현
        # request.data를 통해 전달된 데이터를 사용하여 댓글을 작성하고 저장합니다.
        # 부모 게시글 (BoardPost)의 정보를 가져와 댓글에 연결할 수 있습니다.
        # 댓글을 저장한 후 적절한 응답을 반환합니다.
        return Response({'message': '댓글이 작성되었습니다.'})
    
# Post - Update
class PetsittersPostUpdateView(generics.UpdateAPIView):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer
    lookup_field = 'pk'

    '''
    def put(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        user = Member.objects.get(token=token)
        if token:
            instance = self.get_object()
            print(instance)
            serializer = self.get_serializer(instance)
            print(serializer.data)
            return Response(serializer.data)
        return Response({'error':'로그인이 필요합니다.'})
    '''
    def put(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            return self.update(request, *args, **kwargs)
        return Response({'error':'로그인이 필요합니다.'})

# Post - Delete
class PetsittersPostDestroyView(generics.DestroyAPIView):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            return self.destroy(request, *args, **kwargs)
        return Response({'error':'로그인이 필요합니다.'})

# Post - Comments
class PetsittersCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PetsittersCommentSerializer
    queryset = petsitters_comment.objects.all()

    
# Apply_create
class PetsittersApplyCreateView(APIView):
    def post(self,request):
        token = self.request.headers.get('Authorization')
        print(token)
        if token:
            try:
                user = Member.objects.get(token=token)
                serializer = PetsittersApplyBaseSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(name=user)
                    return Response({'data':serializer.data,'nickname':user.nickname})
                else:
                    return Response({'error':'데이터 맞게보내셈'},status=400)
            except ObjectDoesNotExist:
                return Response({'error':'토큰유효 x'},status=400)
        return Response({'error':'로그인하셈'},status=401)
    
# Apply_retrieve
class PetsittersApplyViewSet(viewsets.ModelViewSet):
    queryset = petsitters_apply.objects.all()
    serializer_class = PetsittersApplyBaseSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PetsittersApplyListSerializer
        return super().get_serializer_class()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        post = get_object_or_404(petsitters_apply, pk=pk)
        serializer = self.get_serializer(post)
        return Response(serializer.data)
    

# Apply_update
class PetsittersApplyUpdateView(generics.UpdateAPIView):
    queryset = petsitters_apply.objects.all()
    serializer_class = PetsittersApplyBaseSerializer
    lookup_field = 'pk'

    '''def get(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({'error':'로그인이 필요합니다.'})
    '''
    def put(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            return self.update(request, *args, **kwargs)
        return Response({'error':'로그인이 필요합니다.'})


# Apply_Delete
class PetsittersApplyDestroyView(generics.DestroyAPIView):
    queryset = petsitters_apply.objects.all()
    serializer_class = PetsittersApplyBaseSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            return Response({'message':'지원서가 삭제되었습니다.'})
        return Response({'error':'로그인이 필요합니다.'})