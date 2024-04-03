from django.urls import path
from . import views

urlpatterns = [
    path('api/private', views.private),
]
