from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from .serializer import BlogSerializer
from rest_framework import viewsets

# Create your views here.

class BlogListView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class DV(APIView):
    authentication_classes = (BasicAuthentication,)
    queryset = Blog.objects.all()
    def get(self, request, pk):
        obj = get_object_or_404(Blog, pk=pk)
        return Response({
            'body':obj.body
        })

class ListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer