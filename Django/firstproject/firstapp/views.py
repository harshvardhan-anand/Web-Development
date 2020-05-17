from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(response):
    return HttpResponse("Hi I am in home page")

def app_home_page(response):
    return HttpResponse("Hi I am app home page, app can be a landing page")

def app_next_page(response):
    return HttpResponse("Hi you have clicked Pricing in app home page")