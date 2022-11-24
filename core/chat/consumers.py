import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.chat_name = self.scope['url_route']['kwargs']['chat_name']
        self.chat_group_name = f'chat_{self.chat_name}'

        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username = text_data_json['username']
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': message,
            }
        )

    async def chat_message(self, event):
        username = event['username']
        message = event['message']

        await self.send(text_data=json.dumps({
            'username': username,
            'message': message,
        }))
