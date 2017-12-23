import json
from six.moves.urllib import request
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend


INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Allow cross-domain requests.
CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}


def _get_public_key(auth0_domain):
    jsonurl = request.urlopen('https://' + auth0_domain + '/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    cert = '-----BEGIN CERTIFICATE-----\n' + jwks['keys'][0]['x5c'][0] + '\n-----END CERTIFICATE-----'
    certificate = load_pem_x509_certificate(cert.encode('utf-8'), default_backend())
    public_key = certificate.public_key()
    return public_key


def jwt_auth(auth0_domain, api_identifier):
    """
        Call this from settings.py only as JWT_AUTH=auth0_settings_jwt_auth(...
    """
    return {
        'JWT_PAYLOAD_GET_USERNAME_HANDLER':
            'drypy.django.auth0.jwt_get_username_from_payload_handler',
        'JWT_PUBLIC_KEY': _get_public_key(auth0_domain),
        'JWT_ALGORITHM': 'RS256',
        'JWT_AUDIENCE': api_identifier,
        'JWT_ISSUER': 'https://' + auth0_domain + '/',
        'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    }
