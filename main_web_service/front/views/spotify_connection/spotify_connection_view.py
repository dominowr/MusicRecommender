from django.views.generic import TemplateView


class SpotifyConnection(TemplateView):
    template_name = 'spotify_connection/spotify_connection.html'

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            pass
        return super().get(request, *args, **kwargs)
