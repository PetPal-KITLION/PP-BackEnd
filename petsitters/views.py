from rest_framework import viewsets, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from accounts.models import Member

from .models import petsitters_post, petsitters_comment
from .serializers import PetsittersPostBaseSerializer, PetsittersPostListSerializer, PetsittersCommentSerializer

from django.shortcuts import get_object_or_404

# Create
class PetsittersPostCreateView(generics.CreateAPIView):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer

    def perform_create(self, serializer):
        # print(self.request.data['member'])
        token = self.request.headers.get('Authorization')
        print(token)
        # member = Member.objects.get(nickname=self.request.user)
        serializer.save()
        
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

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

# Delete
class PetsittersPostDestroyView(generics.DestroyAPIView):
    queryset = petsitters_post.objects.all()
    serializer_class = PetsittersPostBaseSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return Response()

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

