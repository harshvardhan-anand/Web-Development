from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

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

