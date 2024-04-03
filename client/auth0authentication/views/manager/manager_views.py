from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

oauth = OAuth()

oauth.register(
    'auth0',
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        'scope': 'openid profile email',
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse('auth0authentication:callback'))
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session['user'] = token
    if 'spotify' in token['userinfo']['sub']:
        print(token['userinfo']['sub'])
    return redirect(request.build_absolute_uri(reverse('frontend:account')))


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                'returnTo': request.build_absolute_uri(reverse('frontend:index')),
                'client_id': settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )
