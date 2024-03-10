import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from models import Chat, ChatRoom

class poolclient(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "Group_chat"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )  
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        #find room object
        room = await database_sync_to_async(ChatRoom.objects.get)(name=self.roomGroupName)

        #Create new chat object
        chat = Chat(
            content = message
            user = "username"
            room = room
        )

        await database_sync_to_async(chat.save)()

        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message , 
                "username" : username ,
            })  
    async def sendMessage(self , event) : 
        message = event["message"]
        username = event["username"]
        await self.send(text_data = json.dumps({"message":message ,"username":username}))     