from django.urls import path
from .views import IndexView, SpotifyConnection

app_name = 'front'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('spotify-connection', SpotifyConnection.as_view(), name='connection')
]
