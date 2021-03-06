import logging

from django.contrib.auth.models import User, Group
from django.db import transaction


def _logger():
    return logging.getLogger(__name__)


def ensure_user_and_groups(username, groupnames):
    user, created = User.objects.get_or_create(username=username)
    if created:
        _logger().info('Created user:%s' % user)

    if groupnames is None:
        return
    current_groupnames = get_user_groups(user)
    current_groupnames.sort()
    groupnames.sort()
    if current_groupnames != groupnames:
        _set_user_groups(user, current_groupnames, groupnames)


@transaction.atomic
def _set_user_groups(user, current_groupnames, groupnames):
    _logger().info('Set groups for user:{0} current_groupnames:{1} new_groupnames:{2}'.format(user,
                                                                                               current_groupnames,
                                                                                               groupnames))
    user.groups.clear()
    for groupname in groupnames:
        group, created = Group.objects.get_or_create(name=groupname)
        if created:
            _logger().info('Created group:%s' % group)
        group.user_set.add(user)
        _logger().info('Added user %s to group %s' % (user, group))


def get_user_groups(user):
    return list(user.groups.values_list('name', flat=True))