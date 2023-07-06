from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PetsittersCommentViewSet, ToggleLikeAPIView, PetsittersPostViewSet, PetsittersPostCreateView, PetsittersPostUpdateView, PetsittersPostDestroyView, PetsittersCommentCreateView, PetsittersCommentUpdateView, PetsittersCommentDestroyView

router = DefaultRouter()
router.register(r'posts', PetsittersPostViewSet, basename='petsitters-post')
router.register(r'comments', PetsittersCommentViewSet, basename='petsitters-comment')

app_name = 'petsitters'
urlpatterns = [
    path('posts/', PetsittersPostCreateView.as_view(), name='posts-create'),
    path('posts/<int:pk>/update/', PetsittersPostUpdateView.as_view(), name='posts-update'),
    path('posts/<int:pk>/delete/', PetsittersPostDestroyView.as_view(), name='posts-delete'),
    path('posts/<int:pk>/like/', ToggleLikeAPIView.as_view(), name='post-like'),
    path('posts/<int:pk>/comments/', PetsittersCommentCreateView.as_view(), name='comments-create'),
    path('comments/<int:pk>/update/', PetsittersCommentUpdateView.as_view(), name='comments-update'),
    path('comments/<int:pk>/delete/', PetsittersCommentDestroyView.as_view(), name='comments-delete'),
    path('', include(router.urls)),
]