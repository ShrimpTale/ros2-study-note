import rclpy
import requests
from rclpy.node import Node
from example_interfaces.msg import String
#给发布者添加消息类型
from queue import Queue
#线程安全队列，用于按序传递数据

class NovelPubNode(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name}启动')
        #self是NovelPubNode的类，.get_logger()是这个类的方法

        self.novels_queue =Queue()#创建队列,要在调用之前创建

        self.novel_publisher=self.create_publisher(String,'novel',10)
        #创建发布者    ↓                               ↓      ↓     ↓
        #     把发布者保存为属性，以便后续使用         消息类型  话题名称 缓存大小

        self.create_timer(5,self.timer_callback,)
        #                 ↑        ↑ 
        #              间隔几秒   跑回调函数

#       回调函数
    def timer_callback(self):
        #self.novel_publisher.publish
        if self.novels_queue.qsize() >0:
            line =self.novels_queue.get()#获取队列内容
            msg =String()#创建string型消息
            msg.data =line#把队列内容给这个消息
            self.novel_publisher.publish(msg)
            #用发布者把msg发出去
            self.get_logger().info(f'发布了：{msg}')
            

    def download(self,url):
        response =requests.get(url)#下载
        response.encoding='utf-8'
        text =response.text
        #               ↑是response的方法，不是requests的
        self.get_logger().info(f'下载{url},{len(text)}')
        for line in text.splitlines():
            self.novels_queue.put(line)
            #循环把每行小说放入队列


        #不知道是干什么的：
        #text.splitlines()
        #把一串文本分割成列表list,不是ros的消息类型
        #self.novel_publisher.publish
        #调用发布者


def main():
    rclpy.init()

    node =NovelPubNode('novel_pub')
    node.download()#这里放下载网址
    
    rclpy.spin(node)
    rclpy.shutdown()