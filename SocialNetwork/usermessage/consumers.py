# import json
# from channels.channel import Group
#
#
# def ws_connect(message):
#     Group('chat').add(message.reply_channel)
#
#
# def ws_message(message):
#     Group('chat').send({'text': json.dumps({'message': message.content['text'],
#                                             'sender': message.reply_channel.name})})
#
#
# def ws_disconnect(message):
#     Group('chat').discard(message.reply_channel)
# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
