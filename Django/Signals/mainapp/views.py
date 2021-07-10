from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


def register(request):
    '''
    Creating new user.
    This code is just for illustration.
    '''
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cf_password = request.POST.get('cf_password')
        if password == cf_password:
            if not (User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists()):
                User.objects.create_user(username, email, password)
                return HttpResponse('Thanks for registering')

    return render(request, 'register.html')
