"""
ASGI config for websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from websocket import routings
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')

# application = get_asgi_application()

# 支持http和websocket
application = ProtocolTypeRouter({
    "http": get_asgi_application(), # 自动去找url.py,找视图函数
    "websocket": URLRouter(routings.websocket_urlpatterns), # routings.py(url),consumers(view)
})