from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.BookApiView.as_view(), name='book-list')
]
