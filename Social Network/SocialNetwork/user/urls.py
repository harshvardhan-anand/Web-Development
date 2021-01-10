from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload', views.upload, name='upload'),
    path('<str:user_id>/<str:post_id>/', views.dashboard, name='detail_dash'),
    path('likedstatus/', views.like, name='like'),
    path('all-users/', views.user_list, name='user_list'),
    path('<str:username>/', views.user_detail, name='user_detail'),
    path('follow/accepted', views.follow, name='follow')
]