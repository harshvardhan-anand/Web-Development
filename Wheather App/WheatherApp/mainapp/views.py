from django.shortcuts import render,redirect
from django.http import HttpResponse
from mainapp import forms
from mainapp.resources import fetch
import json

# Create your views here.
def homepage(request):
    form = forms.UserParam() # our form
    return render(request,'homepage/homepage.html',context={'form':form})

def ajaxRequest(request):
    return HttpResponse('Hi')

def wheather(request):
    alert = {
        'status':0,
        'msg':'No alert'
    }
    if request.method=='POST':
        if request.is_ajax():
            # if request is ajax the automatically redirect to the wheather link.
            # Since the location is sent through ajax and we have to modify the api call so we need to
            # check wheather the request is ajax or not.
            access = fetch.API(request.POST, is_location_set=1)
            access.api_key = 'ef9bfadddd3a930acfa7d1ee64fc0bef'
        else:
            form = forms.UserParam(request.POST)
            # checking whether form is valid or not
            if form.is_valid():
                user_preference = form.cleaned_data
                access = fetch.API(user_preference,is_location_set=0)
                access.api_key = 'ef9bfadddd3a930acfa7d1ee64fc0bef' #your API key
            else:
                # form is invalid then redirect them to
                # home page with alert fill city properly
                alert['status'] = 1
                alert['msg'] = 'Fill the prefered information properly'
                return redirect('/', context={'alert':alert})
                
        # access the link and fetch the data         
        try:
            wdata = access.wheather_data()
        except:
            # if provided city is incorrect then invalid url will be returned
            # redirect to main page with alert no such city found
            alert['status'] = 1
            alert['msg'] = 'It seems you have misspelled your city. Please try once again.'
            return redirect('/', context={'alert':alert})
        else:
            # otherwise wheather webpage will be returned
            return render(request,'homepage/homepage.html')
    else:
        # if request is a get request then redirect them to home page.
        # this will occur if person want directly goes to homepage/wheather/
        alert['status'] = 1
        alert['msg'] = 'Hey man!! What are you tring to do? Follow the procedure.'
        return redirect('/', context={'alert':alert})