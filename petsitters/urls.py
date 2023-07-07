from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetsittersCommentViewSet, PetsittersPostViewSet, PetsittersPostCreateView, PetsittersPostUpdateView, PetsittersPostDestroyView, PetsittersCommentViewSet, PetsittersApplyCreateView, PetsittersApplyViewSet, PetsittersApplyUpdateView, PetsittersApplyDestroyView

router = DefaultRouter()

app_name = 'petsitters'

urlpatterns = [
    path('posts/', PetsittersPostViewSet.as_view({'get':'list'}), name='posts-list'),
    path('posts/create/', PetsittersPostCreateView.as_view(), name='posts-create'),
    path('posts/<int:pk>/', PetsittersPostViewSet.as_view({'get':'retrieve'}), name='posts-detail'),
    path('posts/<int:pk>/update/', PetsittersPostUpdateView.as_view(), name='posts-update'),
    path('posts/<int:pk>/delete/', PetsittersPostDestroyView.as_view(), name='posts-delete'),

    path('posts/<int:pk>/comments/', PetsittersCommentViewSet.as_view({'post': 'create', 'get': 'retrieve'}),name='comment-list'),

    path('apply/', PetsittersApplyViewSet.as_view({'get':'list'}),name='apply-list'),
    path('apply/create/', PetsittersApplyCreateView.as_view(),name='apply-create'),
    path('apply/<int:pk>/', PetsittersApplyViewSet.as_view({'get':'retrieve'}), name='apply-detail'),
    path('apply/<int:pk>/update/', PetsittersApplyUpdateView.as_view(), name='posts-update'),
    path('apply/<int:pk>/delete/', PetsittersApplyDestroyView.as_view(), name='posts-delete'),
]