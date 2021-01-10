from django.shortcuts import render, redirect,get_object_or_404
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from .models import Contact
from action.utils import create_action

# Create your views here.

def dashboard(request, user_id=None, post_id=None):
    images = Image.objects.all().order_by('-id')
    paginator = Paginator(images, 2)
    page = request.GET.get('page')
    print(request.session.modified)
    try:
        # waw
        images = paginator.page('page')
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    return render(request, 'user/dashboard.html', {'allimages':images})

@login_required
def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            print(request.user)
            form.save(commit=True)
            return redirect('user:dashboard')
    else:
        form = ImageUploadForm()
    return render(request, 'user/upload.html', {'form':form})

# @ajax_required
@require_POST
def like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    print(action)
    print(request.POST)
    if image_id and action:       
        image = Image.objects.get(id=image_id)
        if action =='Like':
            print('liked')
            image.user_like.add(request.user)
        else:
            print('unliked')
            image.user_like.remove(request.user)
        return redirect('user:dashboard')
    return redirect('user:dashboard')

def user_list(request):
    all_users = User.objects.all()
    return render(request, 'user/user_list.html', {'users':all_users})

def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    followers = user.follower.all()
    return render(request, 'user/user_detail.html', {'user':user, 'followers':followers})

@require_POST
def follow(request):
    user1 = request.user
    user2 = request.POST.get('username')
    user2 = User.objects.get(username=user2)
    # user1.following.add(user2)
    Contact.objects.get_or_create(user_from=user1, user_to=user2)
    create_action(user1, 'followed', user2)
    return redirect('user:user_detail', username=user2)
    