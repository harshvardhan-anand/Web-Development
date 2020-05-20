from django.urls import path
from form import views

app_name = 'form'

urlpatterns = [
    path('register', views.register, name='register')
]