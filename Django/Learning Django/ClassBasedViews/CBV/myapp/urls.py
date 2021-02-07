from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('templateview', views.MyTemplateView.as_view(), name='template'),
    path('redirect/<int:pk>', views.Redirect.as_view(), name='redirect'),
    path('redirected-to-me/<int:pk>', views.RedirectedToMe.as_view(), name='redirect_to_me'),    
    path('listview', views.BlogListView.as_view(), name='list'),
    path('detail_view/<int:pk>', views.BlogDetailView.as_view(), name='detail'),
    path('form', views.BasicFormView.as_view(), name='form'),
    path('modelform', views.BlogCreateView.as_view(), name='modelform'),
    path('updateform/<int:pk>', views.BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteObject.as_view(), name='delete')
]