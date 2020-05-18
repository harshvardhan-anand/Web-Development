from django.shortcuts import render
from app.models import PersonDetails
# Create your views here.
def homepage(response):
    return render(response, 'app/homepage.html')