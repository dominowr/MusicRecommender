from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class SpotifyConnection(TemplateView):
    template_name = 'spotify_connection/spotify_connection.html'

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            pass
        return super().get(request, *args, **kwargs)
