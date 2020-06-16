from django.urls import path
from . import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

app_name = 'message'

urlpatterns = [
    # url(r'^all/(?P<message_id>[0-9]+)$', csrf_exempt(views.remove_message)),
    url(r'^delete/(?P<message_id>[0-9]+)$', csrf_exempt(views.remove_message)),
    url(r'^edit/(?P<message_id>[0-9]+)$', csrf_exempt(views.remove_message)),
    url(r'^send/', csrf_exempt(views.send_message), name='send_message'),
    url(r'^list/', views.message_list),
]
#
# urlpatterns = [
#     path('', views.cart_detail, name='cart_detail'),
#     path('add/<int:product_id>/', views.cart_add, name='cart_add'),
#     path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
# ]