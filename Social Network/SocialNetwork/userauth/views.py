from django.shortcuts import render
from .forms import Login, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, 'auth/homepage.html')

def user_login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Now authenticating
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated')
                else:
                    return HttpResponse('User Denied')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = Login()
    return render(request, 'auth/login.html', {'forms':form})

@login_required
def after_authentication(request):
    return render(request, 'auth/authenticated.html')

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            new_user = form.save(commit=False)
            new_user.set_password(cd['password1']) #password1 is the field in the model form
            new_user.save()
            return render(request,'auth/reg_done.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/registration.html', {'form':form})
