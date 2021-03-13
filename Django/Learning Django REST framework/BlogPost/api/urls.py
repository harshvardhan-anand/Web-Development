from django.urls import include, path, re_path
from . import views
from allauth.account.views import confirm_email
from rest_framework.routers import SimpleRouter

app_name = 'api'

urlpatterns = [
    path('', views.ListCreateView.as_view(), name='list-create'),
    path('<int:pk>/', views.RUDView.as_view()),
    path('auth/', include('dj_rest_auth.urls')), # for login and logout
    path('auth/registration', include('dj_rest_auth.registration.urls')),
]

router = SimpleRouter()
router.register('post', views.PostViewSet, basename='post')

urlpatterns+=router.urls