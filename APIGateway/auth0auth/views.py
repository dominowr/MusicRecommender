from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view


@api_view(['GET'])
def login(request):
    url = 'http://127.0.0.1:3000/auth/login'
    return HttpResponseRedirect(url)
