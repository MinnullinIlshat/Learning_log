from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # страница входа
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    # страница выхода
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
]