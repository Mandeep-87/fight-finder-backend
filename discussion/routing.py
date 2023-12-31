from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<pk>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/groupchat/(?P<pk>\d+)/$', consumers.GroupChatConsumer.as_asgi()),
]