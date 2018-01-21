from drypy.django import user

_ACCESS_TOKEN_FIELD_GROUPS = 'https://userinfo/' + 'groups'


def jwt_get_username_from_payload_handler(payload):
    sub = payload.get('sub')  # .replace('|', '.')
    # TODO optimize database access by caching the user
    user.ensure_user_and_groups(sub, payload.get(_ACCESS_TOKEN_FIELD_GROUPS))
    return sub