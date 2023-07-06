from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PetsittersCommentViewSet, ToggleLikeAPIView, PetsittersPostViewSet

router = DefaultRouter()
router.register(r'posts', PetsittersPostViewSet, basename='petsitters-post')
router.register(r'comments', PetsittersCommentViewSet, basename='petsitters-comment')

app_name = 'petsitters'
urlpatterns = [
    path('posts/', PetsittersPostViewSet.as_view({'get': 'list', 'post': 'create'}), name='posts-list'),
    path('posts/<int:pk>/', PetsittersPostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='posts-detail'),
    path('posts/<int:pk>/like/', ToggleLikeAPIView.as_view(), name='post-like'),
    path('posts/detail/', PetsittersPostViewSet.as_view({'get': 'retrieve'}), name='posts-detail'),
    path('', include(router.urls)),
]

