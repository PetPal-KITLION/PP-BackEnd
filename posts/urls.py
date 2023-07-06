from django.urls import path


from .views import BoardPostViewSet, BoardCommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'boardposts', BoardPostViewSet, basename='board_post')
router.register(r'boardcomments', BoardCommentViewSet, basename='board_comment')

urlpatterns = router.urls
