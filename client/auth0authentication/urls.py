from django.urls import path
from . import views

app_name = 'auth0authentication'
urlpatterns = [
    path('login', views.login, name='login'),
    path('callback', views.callback, name='callback'),
    path('logout', views.logout, name='logout'),
]
