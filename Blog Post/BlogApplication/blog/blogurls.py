from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import PostSiteMap
from .feeds import LatestFeed

app_name = 'blog'

sitemaps = {
    'posts':PostSiteMap
}

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # arguments can be captured form URl using angle brackets
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
    path('<int:post_id>', views.post_share, name='post_share'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemap.view.sitemap'),
    path('feed', LatestFeed(), name='post_feed'),
    path('search', views.search, name='search')
]