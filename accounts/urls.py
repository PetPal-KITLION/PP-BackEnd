from django.contrib import admin
from django.urls import path,include,re_path
from .views import SignupView, LoginView, SendMailView, CheckDuplicateView,LogoutView,FindEmailView,ResetPasswordEmailView,ResetPasswordSaveView



urlpatterns=[
    
    path('signup/',SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('member/', CheckDuplicateView.as_view(),name="check"),
    path('email/', SendMailView.as_view(), name="email"),
    path('find-email/', FindEmailView.as_view(),name='findid'),
    path('reset/verify/', ResetPasswordEmailView.as_view(), name="reset-verify"),
    path('reset/password/',ResetPasswordSaveView.as_view(), name="reset-save"),
    
]