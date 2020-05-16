from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(response):
    return HttpResponse("Hi I am in home page")