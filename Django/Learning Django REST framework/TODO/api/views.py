from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from todo_app.models import Todo
from .serializers import TodoSerializer

# Create your views here.
class ListView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer