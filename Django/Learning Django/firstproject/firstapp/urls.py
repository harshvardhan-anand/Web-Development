from django.urls import path
from firstapp import views

urlpatterns = [
    path("", views.app_home_page),
    path("appnextpage/", views.app_next_page)
]