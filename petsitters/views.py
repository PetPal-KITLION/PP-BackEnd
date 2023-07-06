from rest_framework import viewsets, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import petsitters_post, petsitters_comment
from .serializers import PetsittersPostBaseSerializer, PetsittersPostListSerializer, PetsittersCommentSerializer

from django.shortcuts import get_object_or_404

# Create
class PetsittersPostCreateView(generics.CreateAPIView):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)
        
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

# Update
class PetsittersPostUpdateView(generics.UpdateAPIView):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer
    lookup_field = 'pk'

# Delete
class PetsittersPostDestroyView(generics.DestroyAPIView):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer
    lookup_field = 'pk'

# Comments
class PetsittersCommentCreateView(generics.CreateAPIView):
    queryset = petsitters_comment.objects.all()
    serializer_class = PetsittersCommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('pk')
        post = get_object_or_404(petsitters_post, id=post_id)
        serializer.save(post_id=post)

class PetsittersCommentUpdateView(generics.UpdateAPIView):
    queryset = petsitters_comment.objects.all()
    serializer_class = PetsittersCommentSerializer
    lookup_field = 'pk'

class PetsittersCommentDestroyView(generics.DestroyAPIView):
    queryset = petsitters_comment.objects.all()
    serializer_class = PetsittersCommentSerializer
    lookup_field = 'pk'


class PetsittersCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PetsittersCommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return petsitters_comment.objects.filter(post_id=post_id)

class ToggleLikeAPIView(APIView):
    def post(self, request, pk):
        post = get_object_or_404(petsitters_post, id=pk)
        user = request.user

        if post.likes.filter(id=user.id).exists():
            # 이미 좋아요를 눌렀을 경우, 좋아요 제거
            post.likes.remove(user)
            response_data = {'status': 'unliked'}
        else:
            # 좋아요 추가
            post.likes.add(user)
            response_data = {'status': 'liked'}

        return Response(response_data)
