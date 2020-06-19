# from channels.routing import route
# channel_routing = {
#     'websocket.connect': 'chat.consumers.ws_connect',
#     'websocket.receive': 'chat.consumers.ws_message',
#     'websocket.disconnect': 'chat.consumers.ws_disconnect',
# }
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import usermessage.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            usermessage.routing.websocket_urlpatterns
        )
    ),
})