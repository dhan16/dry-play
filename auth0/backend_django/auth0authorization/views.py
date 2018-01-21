from rest_framework.decorators import api_view

from django.http import HttpResponse

import drypy.django.user
from drypy.django.auth0.scope import requires_scope


def public(request):
    return HttpResponse("All good. You don't need to be authenticated to call this")


@api_view(['GET'])
def private(request, username):
    return HttpResponse("Hi {0}. All good. You only get this message if you're authenticated".format(username))


@api_view(['GET'])
@requires_scope('read:messages')
def private_read_messages(request, username):
    return HttpResponse("Hi {0}. All good. You're authenticated and can read messages".format(username))


@api_view(['GET'])
@requires_scope('read:group_messages')
def private_read_groupmessages(request, username):
    groups = drypy.django.user.get_user_groups(request.user)
    return HttpResponse("Hi {0}. All good. You're authenticated and can read messages for the groups {1}"
                        .format( username, " ".join(groups)))
