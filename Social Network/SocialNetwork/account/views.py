from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
import os
from django.conf import settings

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username = cd.get('username'),
                password = cd.get('password')
            )
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('<h1>Authenticated</h1>')
            else:
                return HttpResponse('<h1>Account Disabled</h1>')
        else:
            return HttpResponse('<h1>Invalid User</h1>')
    else:
        form = LoginForm()
    
    return render(request, 'account/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'],
            )
            new_user.save()
            Profile.objects.create(user = new_user)
            return redirect('user:dashboard')
    else:
        user_form = UserRegistrationForm()

    return render(request, 'registration.html', context={'form':user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()           
            messages.success(request, 'Profile Updated Successfully')
            return redirect('user:dashboard')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm()
        profile_form = ProfileEditForm()        
    return render(
        request, 'edit.html', 
        {
            'user_form':user_form,
            'profile_form':profile_form
        }
    )

def grab_info(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user=user)
    old_path = profile.photo.path
    # new_path = fr"{settings.MEDIA_ROOT}/profilepic/{request.user.username}/{filename}"
    print(f'{user}\n')
    print(f'{profile}\n')
    print(f'{old_path}\n')
    # print(f'{new_path}\n')
    return render(request, 'info.html')