"""
ASGI config for privatechat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'privatechat.settings')


from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()


from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter(
    {
        "http":django_asgi_app,
    }
)
