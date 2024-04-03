from django.urls import path
from .views import IndexView, UserDashboardView

app_name = 'frontend'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('account', UserDashboardView.as_view(), name='account'),
]
