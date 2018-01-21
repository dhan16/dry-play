from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/public/', views.public),
    url(r'^api/private/(.*)/', views.private),
    url(r'^api/private_read_messages/(.*)/', views.private_read_messages),
    url(r'^api/private_read_groupmessages/(.*)/', views.private_read_groupmessages),
]
