from django.contrib.auth.models import User
from django.db.utils import IntegrityError


def jwt_get_username_from_payload_handler(payload):
    sub = payload.get('sub').replace('|', '.')
    _ensure_user(sub)
    return sub


def _ensure_user(sub):
    try:
        User.objects.create_user(sub)
    except IntegrityError:
        pass
