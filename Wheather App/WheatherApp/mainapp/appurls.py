from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.wheather,name='wheather')
]