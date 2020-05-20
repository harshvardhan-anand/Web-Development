from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing')
]