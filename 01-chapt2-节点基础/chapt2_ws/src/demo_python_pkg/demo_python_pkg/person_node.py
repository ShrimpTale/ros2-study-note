import rclpy
from rclpy.node import Node
#添加rclpy的node,让person_node成为Node的子类
#注意是rclpy.node ,不要少.node

#定义类:类里有属性方法，可以根据类中的属性方法创建对象，对象属于这个类
#class 类的名字:
class PersonNode(Node):
#                 ↑
#             继承自父类Node
#        init:创建属性后初始化

    def __init__(self,node_name:str,name_value:str,age_value:int) -> None:
    #         传入的对象      参数名。。,类型是。。       不返回任何值,init默认
    #__init__： 希望“对象一创建出来，就自动做点初始化工作”，常见于调用父类 Node 的初始化方法
        super().__init__(node_name)
        #引进父类参数

        self.name=name_value
        self.age=age_value
        #创建方法(在类里的函数)
        #在函数外不能这么操作
    

    def eat(self,food_name:str):
        print("aaa")
        self.get_logger().info("{self.name},{self.age}")
        


def main():
    rclpy.init()
    #因为已经成为Node子类变成节点，故需要跟节点一样的操作

    node =PersonNode('lyy','lyy',78)
    node.eat('ccb')

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':#一般都有
    main()

