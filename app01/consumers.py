import json

from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

CONN_LIST = []


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # 有客户端向后端发送websocket连接请求的时候自动自动触发
        # 服务端允许和客户端创建链接
        print("有人来连接了...")
        host_message = {
            "user": "host",
            "message": "连接成功"
        }

        self.accept()
        CONN_LIST.append(self)
        # 主动给客户端发消息
        self.send(json.dumps(host_message))

    def websocket_receive(self, message):
        # 浏览器基于websocket向后端发送数据，自动触发接收消息
        print("接收到消息———>", message)
        message_data = json.loads(message["text"])
        # return_message = {"user": "host", "message": "不要回复，不要回复，不要回复"}
        return_message = {
            "user": message_data["user"],
            "message": message_data["message"]
        }
        # self 代表与自己创建websocket连接的客户端
        # self.send(json.dumps(return_message))
        for con in CONN_LIST:
            con.send(json.dumps(return_message))


    def websocket_disconnect(self, message):
        # 客户端与服务端断开连接，自动触发
        CONN_LIST.remove(self)
        raise StopConsumer()
