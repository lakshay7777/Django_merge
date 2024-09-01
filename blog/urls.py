from django.urls import path
from . import views



urlpatterns = [
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('post-new/', views.post_new, name='post_new'),
    path('sign-up/', views.userSignUpViews, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('', views.post_list, name='post_list'),
    path('profile-edit/', views.profile_edit, name='profile_edit'), 

    #####################################
   
  

]