from django.shortcuts import render
from django.http import HttpResponse
from mainapp import forms

# Create your views here.
def homepage(request):
    oform = forms.UserParam() # our form
    # print(request.POST['units'])
    return render(request,'homepage/homepage.html',context={'form':oform})

def wheather(request):
    return(HttpResponse('Hey!! its whether link.'))