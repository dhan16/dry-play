from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.utils.six import text_type

from drypy.django.auth0.constants import GUEST

_ACCESS_TOKEN_FIELD_GROUPS = 'https://userinfo/' + 'groups'


class GuestAuthentication(JSONWebTokenAuthentication):
    def authenticate(self, request):
        """
        Returns a two-tuple of User=guest and token=guest if the Authorization header is 'JWT_AUTH_HEADER_PREFIX guest'.
        Otherwise returns `None`.
        """
        jwt_value = self.get_jwt_value(request)
        if not isinstance(jwt_value, text_type):
            jwt_value = jwt_value.decode()
        if jwt_value != GUEST:
            return None
        user = self.authenticate_credentials({'sub': GUEST})
        return (user, jwt_value)
