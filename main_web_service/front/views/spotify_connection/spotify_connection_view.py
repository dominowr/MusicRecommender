from django.shortcuts import redirect
from django.views.generic import TemplateView
import json


class SpotifyConnection(TemplateView):
    template_name = 'spotify_connection/spotify_connection.html'

    def post(self, request, *args, **kwargs):
        url = 'http://127.0.0.1:5000/api/hello/'
        return redirect(url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'session': self.request.session.get('user'),
            'pretty': json.dumps(self.request.session.get('user'), indent=4)
        }
        return context

