from django.shortcuts import render

# Create your views here.
def homepage(response):
    return render(response, 'app/homepage.html')