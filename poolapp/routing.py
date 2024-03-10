from django.urls import path, include
from poolapp.consumers import poolclient

websocket_urlpatterns = [
    path("", poolclient.as_asgi()),
]