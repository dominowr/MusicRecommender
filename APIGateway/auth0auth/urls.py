from django.urls import path
from . import views

app_name = 'auth0auth'
urlpatterns = [
    path('login', views.login, name='login'),
]