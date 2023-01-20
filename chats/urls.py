from django.urls import path
from . import views
import secrets
import random


a = secrets.token_urlsafe(10)
b = list(a)
random.shuffle(b)
c = ''.join(b)

urlpatterns = [
    path('',views.Index.as_view(),name="index"),
    path('chat/' + c + '/<slug:username>',views.chatPage,name="chat"),
    
]
