import jwt
import json
from functools import wraps

from django.conf import settings
from django.http import HttpResponse
from six.moves.urllib import request as req
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

ACCESS_TOKEN_FIELD_GROUPS = 'https://userinfo/' + 'groups'


def get_token_auth_header(request):
    """Obtains the access token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token


def _has_scope(request, required_scope):
    """Determines if the required scope is present in the access token
        Args:
            request
            required_scope (str): The scope required to access the resource
        """
    token = get_token_auth_header(request)
    AUTH0_DOMAIN = settings.AUTH0_DOMAIN
    API_IDENTIFIER = settings.API_IDENTIFIER
    jsonurl = req.urlopen('https://' + AUTH0_DOMAIN + '/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    cert = '-----BEGIN CERTIFICATE-----\n' + jwks['keys'][0]['x5c'][0] + '\n-----END CERTIFICATE-----'
    certificate = load_pem_x509_certificate(cert.encode('utf-8'), default_backend())
    public_key = certificate.public_key()
    decoded = jwt.decode(token, public_key, audience=API_IDENTIFIER, algorithms=['RS256'])

    if decoded.get("scope"):
        token_scopes = decoded["scope"].split()
        for token_scope in token_scopes:
            if token_scope == required_scope:
                request.auth = decoded
                return True
    return False


def requires_scope(required_scope):
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not _has_scope(args[0], required_scope):
                return HttpResponse("You don't have access to this resource")
            return f(*args, **kwargs)
        return decorated
    return require_scope


def user_groups(request):
    return request.auth[ACCESS_TOKEN_FIELD_GROUPS]


def requires_scope_and_group(required_scope):
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not _has_scope(args[0], required_scope):
                return HttpResponse("You don't have access to this resource")
            groups = user_groups(args[0])
            if not groups or len(groups) == 0:
                return HttpResponse("Add yourself to a group first")
            return f(*args, **kwargs)
        return decorated
    return require_scope