from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import *
from channels.db import database_sync_to_async
from .models import Message
import datetime



class ChatConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def save_message(self,sender,content,room):
        msg =  Message.objects.create(sender=sender,content=content,room=room)
        msg.save()
    
    async def connect(self):
        user1_tag = self.scope['user'].username
        user2_tag = self.scope['url_route']['kwargs']['username']
        user_list = [user1_tag,user2_tag]
        user_list.sort()
        user_list = ''.join(user_list)
        self.room_name = user_list

        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username = text_data_json['username']
        message = text_data_json['message']
        timestamp = datetime.datetime.now().isoformat()

        await self.save_message(sender=self.scope['user'],content=message,room=self.room_name)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chatMessage',
                'username':username,
                'message':message,
                'timestamp':timestamp
            }
        )  

    async def chatMessage(self,event):
        username = event['username']
        message = event['message']
        timestamp = event['timestamp']

        await self.send(text_data=json.dumps(
            {
                'username':username,
                'message':message,
                'timestamp':timestamp
            }
        ))