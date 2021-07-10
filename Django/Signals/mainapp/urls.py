from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.register, name='register')
]
