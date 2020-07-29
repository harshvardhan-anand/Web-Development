from django.urls import path
from mainapp import views

urlpatterns = [
    path('',views.wheather,name='wheather')
]