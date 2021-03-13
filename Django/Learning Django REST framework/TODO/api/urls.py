from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('', views.ListView.as_view(), name='list-view'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail-view'),
]
