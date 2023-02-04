from django.urls import re_path,path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<username>[^/]+)/$',ChatConsumer.as_asgi()),
]