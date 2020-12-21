from os import name
from django.urls import path
from django.urls.base import reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'userauth'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('login', views.user_login, name='login')
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('authenticated', views.after_authentication, name='authenticated'),
    path('change_password', auth_views.PasswordChangeView.as_view(
        success_url = reverse_lazy('userauth:paw-ch-done')
    ), name='password-change'),
    path('psw-change-done', auth_views.PasswordChangeDoneView.as_view(), name='paw-ch-done'),
    path('register', views.registration, name='registration')
]