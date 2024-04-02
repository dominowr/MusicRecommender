from django.views.generic import TemplateView
from django.shortcuts import redirect
import json


class IndexView(TemplateView):
    template_name = 'index/index.html'

    # def post(self, request):
    #     url = 'http://127.0.0.1:5000/api/login'
    #     return redirect(url)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {
    #         'session': self.request.session.get('user'),
    #         'pretty': json.dumps(self.request.session.get('user'), indent=4)
    #     }
    #     return context
