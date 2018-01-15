from functools import wraps

from django.http import HttpResponse
from rest_framework_jwt import authentication

from drypy.django.auth0.constants import GUEST


def _get_token_auth_header(request):
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
    token = _get_token_auth_header(request)
    if token == GUEST:
        return False
    decoded = authentication.jwt_decode_handler(token)
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