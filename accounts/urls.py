from django.contrib import admin
from django.urls import path,include,re_path
from .views import SignupView, LoginView, SendMailView, CheckDuplicateView



urlpatterns=[
    
    path('signup/',SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('member/', CheckDuplicateView.as_view(),name="check"),
    path('email/', SendMailView.as_view(), name="email"),
    # 이메일 관련 필요
]