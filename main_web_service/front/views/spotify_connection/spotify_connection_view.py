from django.views.generic import TemplateView


class SpotifyConnection(TemplateView):
    template_name = ''

    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            pass
        return super().get(request, *args, **kwargs)
