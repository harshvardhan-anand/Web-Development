from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dethomepage/<int:pk>', views.dethomepage, name='dethomepage'), 
    path('post', views.post, name='post'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete')
]