from django.urls import re_path
from app01 import consumers

websocket_urlpatterns = [
    re_path(r'^room/(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
