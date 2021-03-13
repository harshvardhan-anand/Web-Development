from django.shortcuts import render, get_object_or_404
from .serializer import PostSerializer
from rest_framework import generics, permissions, viewsets
from post.models import Post
from .permissions import IsAuthorOrReadOnly
from django.views.generic import TemplateView

# Create your views here.
class ListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# retrive update delete view
class RUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly,]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# Viewset
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer