from django.urls import path
from . import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

app_name = 'friendlist'

urlpatterns = [
    # url(r'^delete/(?P<message_id>[0-9]+)$', csrf_exempt(views.remove_message)),
    # url(r'^add/', csrf_exempt(views.send_message), name='add_friend'),
    url(r'^list/(?P<user_id>[0-9]+)$', views.friend_list, name="friend_list"),
]
