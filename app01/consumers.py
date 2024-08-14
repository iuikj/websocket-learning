import json

from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # 有客户端向后端发送websocket连接请求的时候自动自动触发
        # 服务端允许和客户端创建链接
        print("有人来连接了...")
        host_message = {
            "user": "host",
            "message": "连接之后主动发送"
        }

        self.accept()

        # 将这客户端的连接对象加入到某个地方（内存或redis）
        async_to_sync(self.channel_layer.group_add)("12306", self.channel_name)
        # 主动给客户端发消息
        self.send(json.dumps(host_message))

    def websocket_receive(self, message):
        # 浏览器基于websocket向后端发送数据，自动触发接收消息
        print("接收到消息———>", message)
        return_message = {"user": "host", "message": "不要回复，不要回复，不要回复"}
        # self 代表与自己创建websocket连接的客户端
        # self.send(json.dumps(return_message))

        # 通知组内所有客户端，执行xx.oo方法，在此方法中可以实现任意的功能
        async_to_sync(self.channel_layer.group_send)(
            "12306",
            {
                "type": "xx.oo",
                "message": message
            }
        )

    # 这里的下划线_,代表点即xx.oo
    def xx_oo(self, event):
        data=json.loads(event['message']['text'])
        message=data['message']
        user=data['user']
        return_message = {"user": user, "message": message}
        self.send(json.dumps(return_message))

    def websocket_disconnect(self, message):
        # 客户端与服务端断开连接，自动触发
        raise StopConsumer()
