from django.urls import path
from speechapp import views

app_name = 'speechapp'

urlpatterns = [
    path('', views.homepage, name='homepage')
]