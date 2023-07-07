from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import BoardPostCreateView, BoardPostBaseViewSet, BoardPostUpdateView, BoardPostDestroyView, BoardCommentViewSet


router = DefaultRouter()

#app_name = 'posts'

urlpatterns = [
    path('board/',BoardPostBaseViewSet.as_view({'get':'list'}), name='board-list'),
    path('board/create/', BoardPostCreateView.as_view(), name='board-crate'),
    path('board/<int:pk>/', BoardPostBaseViewSet.as_view({'get':'retrieve'}), name='board-detail'),
    path('board/<int:pk>/update/', BoardPostUpdateView.as_view(), name='board-update'),
    path('board/<int:pk>/delete/', BoardPostDestroyView.as_view(), name='board-delete'),
]
