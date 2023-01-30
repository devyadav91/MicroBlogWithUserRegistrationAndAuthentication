from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('about',views.about,name='about'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('signup',views.user_signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('postarticle',views.PostForm,name='postarticle'),
    path('updatepost/<int:pk>',views.UpdatePost,name='updatepost'),
    path('deletepost/<int:pk>',views.DeletePost,name='deletepost'),
        
]
