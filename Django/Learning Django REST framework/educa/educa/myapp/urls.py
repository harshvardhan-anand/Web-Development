from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', views.ListViewset)

app_name = 'myapp'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='listview'),
    path('detail/<int:pk>', views.DV.as_view()),
    path('v', include(router.urls))
]