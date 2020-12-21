from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post

class LatestFeed(Feed):
    title = 'RSS feed title'
    link = reverse_lazy('blog:post_list')
    decription= 'RSS feed decription'

    def items(self):
        items = Post.published.all()[:5]
        return items

    def item_title(self, post):
        return post.title

    def item_description(self, post):
        return truncatewords(post.body, 30)
