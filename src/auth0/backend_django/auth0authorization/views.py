from rest_framework.decorators import api_view

from django.http import HttpResponse

import drypy.django.user
from drypy.django import auth0
from drypy.django.auth0 import requires_scope


def public(request):
    return HttpResponse("All good. You don't need to be authenticated to call this")


@api_view(['GET'])
def private(request):
    return HttpResponse("All good. You only get this message if you're authenticated")


@api_view(['GET'])
@requires_scope('read:messages')
def private_read_messages(request):
    return HttpResponse("All good. You're authenticated and can read messages")


@api_view(['GET'])
@requires_scope('read:group_messages')
def private_read_groupmessages(request):
    groups = drypy.django.user.get_user_groups(request.user)
    return HttpResponse("All good. You're authenticated and can read messages for the groups %s" % " ".join(groups))
