"""
ASGI config for roomproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roomproject.settings')

#application = get_asgi_application()
django_asgi_app = get_asgi_application()

# from channels.routing import ProtocolTypeRouter

# from channels.routing import URLRouter
# from channels.auth import AuthMiddlewareStack
# from chat import routing

# application = ProtocolTypeRouter( {
#     'http': get_asgi_application(),
#     'websocket': AuthMiddlewareStack( URLRouter( routing.websocket_urlpatterns ) ),
# } )