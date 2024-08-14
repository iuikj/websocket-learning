import json

from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # 有客户端向后端发送websocket连接请求的时候自动自动触发
        # 服务端允许和客户端创建链接
        print("有人来连接了...")
        host_message={
            "user": "host",
            "message": "连接之后主动发送"
        }


        self.accept()
        # 主动给客户端发消息
        self.send(json.dumps(host_message))

    def websocket_receive(self, message):
        # 浏览器基于websocket向后端发送数据，自动触发接收消息
        print("接收到消息———>", message)
        return_message = {"user": "host", "message": "不要回复，不要回复，不要回复"}
        # self 代表与自己创建websocket连接的客户端
        self.send(json.dumps(return_message))
        # self.close()

    def websocket_disconnect(self, message):
        # 客户端与服务端断开连接，自动触发
        raise StopConsumer()
