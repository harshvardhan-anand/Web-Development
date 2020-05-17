from django.shortcuts import render

# Create your views here.
def homepage(response):
    return render(response, "homepage.html")

def about(response):
    return render(response, "about.html")