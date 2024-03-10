import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from .models import Taskping

class StatusUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'client_group'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if 'action' in text_data_json and text_data_json['action'] == 'update_task_status':
            task_id = text_data_json.get('task_id')
            await self.update_task_status(task_id)

    async def send_task_update(self, event):
        # Handle sending the update to the WebSocket
        await self.send(json.dumps({
            'type': 'task_update',  # This is what the client JavaScript will look for
            'task': event['task']
        }))

    @database_sync_to_async
    def update_task_status(self, task_id):
        try:
            task = Taskping.objects.get(pk=task_id)
            task.status = 'y'
            task.save()
            return True
        except Taskping.DoesNotExist:
            return False
