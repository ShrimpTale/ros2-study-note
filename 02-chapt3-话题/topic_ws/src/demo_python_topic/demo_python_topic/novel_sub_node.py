import espeakng
import rclpy
from rclpy.node import Node
import requests
from example_interfaces.msg import String
from queue import Queue

class NovelSubNode(Node):
    def __init__ (self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name}启动')
        self.novel_queue =Queue()
        #创建队列放接受的内容
        self.novel_subscriber =self.create_subscription(String,'novel',novel_callback,10)
        #创建订阅者      ↑                                    ↑      ↑            ↑
        #        把订阅者保存为属性，以便后续使用              消息类型 话题名 回调函数(收到数据后做什么)
        

    def novel_callback(self,msg):
        #                    ↑传过来的msg
        self.novel_queue.put(msg.data)
        #把过来的msg里的data(内容)放进来，msg本身是一个string


def main():
    rclpy.init()
    node =NovelSubNode('novel_sub')
    rclpy.spin(node)
    rclpy.shutdown()