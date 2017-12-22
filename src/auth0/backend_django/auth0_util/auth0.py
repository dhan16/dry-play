import logging

from functools import wraps

from django.contrib.auth.models import User, Group
from django.db import transaction
from django.http import HttpResponse
from rest_framework_jwt import authentication


_ACCESS_TOKEN_FIELD_GROUPS = 'https://userinfo/' + 'groups'


def _logger():
    return logging.getLogger('auth0_util')


def jwt_get_username_from_payload_handler(payload):
    sub = payload.get('sub').replace('|', '.')
    _ensure_user_and_groups(sub, payload.get(_ACCESS_TOKEN_FIELD_GROUPS))
    return sub


# TODO optimize database access by caching the user
def _ensure_user_and_groups(username, groupnames):
    user, created = User.objects.get_or_create(username=username)
    if created:
        _logger().debug('Created user:%s' % user)

    current_groupnames = get_user_groups(user)
    current_groupnames.sort()
    groupnames.sort()
    if current_groupnames != groupnames:
        _set_user_groups(user, current_groupnames, groupnames)


@transaction.atomic
def _set_user_groups(user, current_groupnames, groupnames):
    _logger().debug('Set groups for user:{0} current_groupnames:{1} new_groupnames:{2}'.format(user,
                                                                                               current_groupnames,
                                                                                               groupnames))
    # ' '.join(current_groupnames), ' '.join(groupnames))
    user.groups.clear()
    for groupname in groupnames:
        group, created = Group.objects.get_or_create(name=groupname)
        if created:
            _logger().debug('Created group:%s' % group)
        group.user_set.add(user)
        _logger().debug('Added user %s to group %s' % (user, group))


def get_user_groups(user):
    return list(user.groups.values_list('name', flat=True))


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