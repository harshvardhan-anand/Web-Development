from django.shortcuts import render, reverse
from django.shortcuts import get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailForm, CommentForm
from django.http import HttpResponseRedirect
from taggit.models import Tag
from django.db.models import Count

# Create your views here.
def post_list(request, tag_slug=None):
    all_post = Post.published.all()
    tag=None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        all_post = all_post.filter(tags=tag)
    paginator = Paginator(all_post, 4) # per page 4 posts
    page = request.GET.get('page')
    print(f'\n{page}\n')
    try:
        all_post = paginator.page(page)
    except PageNotAnInteger:
        all_post = paginator.page(1)
    except EmptyPage:
        all_post = paginator.page(paginator.num_pages)
    return render(request, 'blog/postList.html', {'posts':all_post, 'tag':tag}) #here we have "posts" as context variable

def post_detail(request, year, month, day, slug):
    # filtering on the r̥basis of day, month, year
    post = get_object_or_404(Post, slug=slug, publish__day=day, publish__month=month, publish__year=year)
    all_comments = post.comments.all()
    show_comment_form = False
    try:
        if request.session['comment']:
            request.session['comment'] = False
            form = CommentForm()
            show_comment_form = True
        elif request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = post
                new_comment.save()
        else:
            form = None
    except:
        form = None
    
    # RECOMMENDING SIMILAR POSTS
    # https://stackoverflow.com/questions/35114737/how-do-you-add-similar-posts-to-a-detail-page-using-django
    similar_posts = post.tags.similar_objects()[:5]
    return render(
        request, 'blog/postDetail.html', 
        context={
            'post':post, 
            'form':form, 
            'all_comments':all_comments, 
            'showCommentForm':show_comment_form,
            'similar_posts':similar_posts
        }
    ) #here we have "post" as context variable

def share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    shared = False
    if request.method == 'POST':
        # submitted form
        form = EmailForm(request.POST)
        if form.is_valid():
            shared = True
            cd = form.cleaned_data
            print(cd)
    else:
        form = EmailForm()
    return render(request, 'blog/postDetail.html', {'post':post, 'shared':shared, 'form':form})

def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    request.session['comment'] = True
    # reverse return a string so we need to use HttpRedirect, 
    # else you will get -->'str' object has no attribute 'get'<-- error.
    return HttpResponseRedirect(reverse('blog:post_detail', kwargs={
        'year' : post.publish.year,
        'month' : post.publish.month,
        'day' : post.publish.day,
        'slug' : post.slug
    }))

def search(request):
    contains = request.GET.get('query')
    # we will save all the published post in a variable to
    # avoid hitting database again and again.
    all_post = Post.published.all()
    # The way we are doing multiple field search 
    # can be done more efficiently with postgres search vector
    post_contains = all_post.filter(body__contains=contains)
    title_contains = all_post.filter(title__contains=contains)
    count = post_contains.count()+title_contains.count()
    return render(
        request, 'blog/search.html',
        context={
            'post_contains':post_contains,
            'title_contains':title_contains,
            'count':count,
            'query':contains
        }
    )