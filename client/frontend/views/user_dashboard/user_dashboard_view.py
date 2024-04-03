import requests
from django.shortcuts import redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView
import json


class UserDashboardView(TemplateView):
    template_name = 'user_dashboard/user_dashboard.html'
    url = 'http://127.0.0.1:3000/api/private'

    def get(self, request, *args, **kwargs):

        token = request.session.get('user')['access_token']
        headers = {'Authorization': f'Bearer {token}'}

        response = requests.get(self.url, headers=headers)

        if response.status_code == 200:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('auth0authentication:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'session': self.request.session.get('user'),
            'pretty': json.dumps(self.request.session.get('user'), indent=4)
        }
        return context
