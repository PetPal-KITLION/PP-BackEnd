from rest_framework import viewsets, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

#from accounts.models import Member

from .models import petsitters_post, petsitters_comment, petsitters_apply
from .serializers import PetsittersPostBaseSerializer, PetsittersPostListSerializer, PetsittersCommentSerializer, PetsittersApplyBaseSerializer, PetsittersApplyListSerializer

from django.shortcuts import get_object_or_404

# Post - Create
class PetsittersPostCreateView(generics.CreateAPIView):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer

    def perform_create(self, serializer):
        token = self.request.headers.get('Authorization')
        if token:
            serializer.save()
            return Response({'message':'글이 등록되었습니다.'})
        return Response({'error':'로그인이 필요합니다.'})

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

# Post - Update
class PetsittersPostUpdateView(generics.UpdateAPIView):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({'error':'로그인이 필요합니다.'})

# Post - Delete
class PetsittersPostDestroyView(generics.DestroyAPIView):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            return Response({'message':'글이 삭제되었습니다.'})
        return Response({'error':'로그인이 필요합니다.'})

# Post - Comments
class PetsittersCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PetsittersCommentSerializer
    queryset = petsitters_comment.objects.all()

    
# Apply_create
class PetsittersApplyCreateView(generics.CreateAPIView):
    queryset = petsitters_apply.objects.all()
    serializer_class = PetsittersApplyBaseSerializer

    def post(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            return self.create(request, *args, **kwargs)
            return Response({'message':'지원서가 접수되었습니다.'})
        return Response({'error':'로그인이 필요합니다.'})
    
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

    def get(self, request, *args, **kwargs):
        token = self.request.headers.get('Authorization')
        if token:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
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