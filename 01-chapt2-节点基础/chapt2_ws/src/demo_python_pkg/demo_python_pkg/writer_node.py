from person_node import PersonNode
import rclpy
# 这一行 from rclpy.node import Node 删掉，你父类已经继承了，子类不需要再导

class WriterNode(PersonNode):
    def __init__(self, node_name: str, name: str, age: int, book: str) -> None:
        # 按照父类要求的顺序传：节点名、名字、年龄
        super().__init__(node_name, name, age)
        #必须把父类所有的参数放进来再写自己的
        self.book = book

def main():
    rclpy.init()
    # 第一个参数 'sb' 是给 ROS 系统看的节点名
    # 第二个参数 'sb' 是人的名字，第三个 91 是年 龄，第四个 'shu' 是书
    node = WriterNode('sb', 'sb', 91, 'shu')
    node.eat('shi')

    rclpy.spin(node)
    node.destroy_node()  #返还系统资源
    rclpy.shutdown()

if __name__ == '__main__':
    main()#一般都有