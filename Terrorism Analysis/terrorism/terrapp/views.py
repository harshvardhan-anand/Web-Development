from django.shortcuts import render
from .forms import UserData

# Create your views here.

def home(request):
    return render(request, 'form.html', context={'form':UserData()})