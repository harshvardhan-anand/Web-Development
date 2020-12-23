from django.urls import path
from . import views
from .feeds import LatestPosts
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # see here we have placed "published" at the begining but we dont have to put that in <a> tag in postList.html
    # because we are using cannonical url which uses reverse so we dont care about the link
    path('published/<int:year>/<int:month>/<int:day>/<slug:slug>',views.post_detail, name='post_detail'),
    # django will use the name to call the view and dynamically change the URI
    path('published/share/<int:post_id>', views.share, name='share'),
    path('searchBy/tag/<slug:tag_slug>', views.post_list, name='tagClick'),
    path('feed/', LatestPosts(), name='feed'),
    path('search/', views.search, name='search')
]