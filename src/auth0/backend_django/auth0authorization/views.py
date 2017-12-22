from rest_framework.decorators import api_view

from auth0authorization.auth0 import *

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
    groups = get_user_groups(request.user)
    return HttpResponse("All good. You're authenticated and can read messages for the groups %s" % " ".join(groups))
