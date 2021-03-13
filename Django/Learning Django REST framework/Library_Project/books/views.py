from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book

# Create your views here.
class Home(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'