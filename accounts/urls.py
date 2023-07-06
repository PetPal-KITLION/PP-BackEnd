from django.contrib import admin
from django.urls import path,include,re_path
from .views import SignupView, LoginView, SendMailView, CheckDuplicateView,LogoutView,FindEmailView



urlpatterns=[
    
    path('signup/',SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('member/', CheckDuplicateView.as_view(),name="check"),
    path('email/', SendMailView.as_view(), name="email"),
    path('findid/', FindEmailView.as_view(),name='findid'),
    
]