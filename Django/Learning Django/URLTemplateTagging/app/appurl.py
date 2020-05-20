from django.urls import path
from app import views

# Used for template tagging
# Django will look for this variable automatically
app_name = "app"

#  name parameter is important as if you have two app with same link say 
# "pricing" then django will get confused.
urlpatterns = [
    path('signin/', views.signin, name='signin'), 
    path('pricing/', views.pricing, name='pricing'),
]