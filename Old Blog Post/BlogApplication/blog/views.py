from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import EmailPostForm, CommentForm, SearchForm
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def post_list(request):
    post = Post.published.all()
    # print(type(post[0])) # class is represented in its string form with the help of __str__ defied in model
    paginator = Paginator(post, 1)
    page = request.GET.get('page')
    # print(page)
    # print(request.GET)
    search = SearchForm()
    try:
        post_to_serve = paginator.page(page)
    except PageNotAnInteger:
        post_to_serve = paginator.page(1)
        # print(type(post_to_serve))  #<class 'django.core.paginator.Page'>
    except EmptyPage:
        post_to_serve = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', {'posts':post_to_serve, 'search':search})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, publish__day=day, publish__month=month, publish__year=year)
    # print(post) # title
    # print(type(post))
    all_comments = post.comment_related_to_post.filter(active=True)
    new_comment = None
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.active = True
            new_comment.save()
            # print(new_comment) # output str value of Comment class
    else:
        form = CommentForm()
    return render(request, 'blog/detail.html', {'posts':post, 'form':form, 'new_comment':new_comment,
                    'all_comments':all_comments})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            print(post_url)
            #... send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html', {'post':post, 'form':form})

def search(request):
    print(request)
    # print(reverse('blog:search')) #/search
    # print(reverse('blog:search')) # /
    return HttpResponseRedirect(reverse('blog:post_list'))