from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    #path('ws/providertracking/', consumers.StatusUpdateConsumer.as_asgi()),
    path('ws/clienttracking/', consumers.StatusUpdateConsumer.as_asgi()),
    # Add other WebSocket URL patterns as needed
]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
