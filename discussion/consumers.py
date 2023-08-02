
import json
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from .models import Chat,User, GroupChatMessage
from asgiref.sync import sync_to_async
# from discussion.serializers import UserSerializer
from .serializers import ConsumerDetailSerializers


@sync_to_async
def get_all_users(data_to_get):
    sender = User.objects.get(id=data_to_get['text']['sender'])
    receiver = User.objects.get(id=data_to_get['text']['receiver'])
    chat = Chat.objects.create(
        is_seen=data_to_get['text']['is_seen'],
        sender_id=data_to_get['text']['sender'],
        receiver_id=data_to_get['text']['receiver'],
        chat=data_to_get['text']['chat']
    )
    return {
        'chat': chat,
        'sender': ConsumerDetailSerializers(sender).data,
        'receiver': ConsumerDetailSerializers(receiver).data
    }


class ChatConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self,event=None):
            await self.accept()
            await self.send(json.dumps({
                        "type":"websocket.send",
                        "text":"Successfully connected"
                    }))
            self.room_name = f'chat-by-{self.scope["url_route"]["kwargs"]["pk"]}'
            self.room_group_name = f'chat_users_group-{self.scope["url_route"]["kwargs"]["pk"]}'
            await self.channel_layer.group_add(self.room_group_name,self.channel_name)

    async def websocket_receive(self, event):
        data_to_get = json.loads(event['text'])
        if data_to_get:
            result = await get_all_users(data_to_get)
            data_to_get['sender'] = result['sender']
            data_to_get['receiver'] = result['receiver']
            data_to_get['chat'] = data_to_get['text']['chat']
            data_to_get['is_seen'] = data_to_get['text']['is_seen']
        
        self.room_group_name = f'chat_users_group-{self.scope["url_route"]["kwargs"]["pk"]}'
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_msg",
                "value": data_to_get
            }
    )
    #     await channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             "type": "chat_msg",
    #             "value": data_to_get
    #         }
    # )

    async def websocket_disconnect(self,event):
            print('disconnect')
            print(event)


    # async def chat_msg(self, event):
    #     data_to_send = {
    #         "type": "websocket.send",
    #         "data": event
    #     }

    #     sender_id = event['value']['sender']['id']
    #     receiver_id = event['value']['receiver']['id']
    #     current_user_id = self.scope['user'].id  # Assuming the user is authenticated

    #     # Check if the message is sent by the current user
    #     if sender_id != current_user_id:
    #         # Add sender and receiver details
    #         data_to_send['data']['value']['sender'] = event['value']['sender']
    #         data_to_send['data']['value']['receiver'] = event['value']['receiver']
    #         await self.send(json.dumps(data_to_send))        

    async def chat_msg(self, event):
        data_to_send = {
            "type": "websocket.send",
            "data": event
        }

        # Add sender and receiver details
        data_to_send['data']['value']['sender'] = event['value']['sender']
        data_to_send['data']['value']['receiver'] = event['value']['receiver']
        
        await self.send(json.dumps(data_to_send))



















class GroupChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def save_group_chat_message(self, sender, receiver, message):
        return GroupChatMessage.objects.create(
            # room_group_name=room_group_name,
            sender_id=sender,
            receiver_id=receiver,
            message=message
        )

    async def websocket_connect(self, event=None):
        await self.accept()
        await self.send(json.dumps({
            "type": "websocket.send",
            "text": "Successfully connected"
        }))
        self.room_group_name = f'chat_users_group-{self.scope["url_route"]["kwargs"]["pk"]}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

    async def websocket_receive(self, event):
        data_to_get = json.loads(event['text'])
        print("----------------",data_to_get)
        if data_to_get:
            await self.save_group_chat_message(
                # self.room_group_name,
                data_to_get['text']['sender'],
                data_to_get['text']['receiver'],
                data_to_get['text']['message']
            )

        self.room_group_name = f'chat_users_group-{self.scope["url_route"]["kwargs"]["pk"]}'
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_msg",
                "value": data_to_get
            }
        )

    async def chat_msg(self, event):
        data_to_send = {
            "type": "websocket.send",
            "data": event
        }
        print(data_to_send,'8888888888888888888888888')
        await self.save_group_chat_message(
            # self.room_group_name,
            data_to_send['data']['value']['text']['sender'],
            data_to_send['data']['value']['text']['receiver'],
            data_to_send['data']['value']['text']['message']
        )
        await self.send(json.dumps(data_to_send))


