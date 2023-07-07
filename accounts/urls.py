from django.contrib import admin
from django.urls import path,include,re_path
from .views import SignupView, LoginView, SendMailView, CheckDuplicateView,LogoutView,FindEmailView,ResetPasswordEmailView,ResetPasswordSaveView,MyProfileView,RegistPetView,ReviewCreateView,ReviewListView,DeleteMember,EditProfileView



urlpatterns=[
    
    path('signup/',SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('delete/', DeleteMember.as_view(),name="delete_user"),
    path('member/', CheckDuplicateView.as_view(),name="check"),
    path('email/', SendMailView.as_view(), name="email"),
    path('find-email/', FindEmailView.as_view(),name='findid'),
    path('reset/verify/', ResetPasswordEmailView.as_view(), name="reset_verify"),
    path('reset/password/',ResetPasswordSaveView.as_view(), name="reset_save"),
    path('profile/',MyProfileView.as_view(), name="profile"),
    path('profile/edit/',EditProfileView.as_view(), name="edit_profile"),
    path('pets/create/',RegistPetView.as_view(),name="regist_pet"),
    path('review/',ReviewListView.as_view(),name="list_review"),
    path('review/create/',ReviewCreateView.as_view(),name="create_review"),
    
    
]