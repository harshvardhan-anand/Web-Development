from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.Home.as_view(), name='home')
]
