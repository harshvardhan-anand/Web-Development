from django import template
from ..models import Post

register = template.Library()

@register.inclusion_tag('blog/latestPost.html')
def latest_post(nos = 5):
    lp = Post.published.order_by('-publish')[:nos]
    return {'latest_post':lp}

@register.inclusion_tag('navBar.html')
def navbar():
    return None