"""
ASGI config for poolapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import poolcleanapp.routing
from channels.security.websocket import AllowedHostsOriginValidator


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poolapp.settings")
django_asgi_app = get_asgi_application()
import poolapp.routing



application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AllowedHostsOriginValidator(
    AuthMiddlewareStack(
         URLRouter(
            poolcleanapp.routing.websocket_urlpatterns
        )))
})
