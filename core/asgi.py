"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
from home.consumers import MyConsumer, NewConsumer
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import include,path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

ws_patterns = [
    path("ws/test/" , MyConsumer),
    path("ws/new/" , NewConsumer)

]

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter(ws_patterns)        
    )

})

