from person_node import PersonNode
#此物是Node的子类 
import rclpy
#不需要from rclpy.node import Node，父类已经继承了，子类不需要再导
#这个import是为了这个文件加的

class WriterNode(PersonNode):
    def __init__(self, node_name: str, name: str, age: int, book: str) -> None:
        # 按顺序拿父类里需要的+建自己的
        super().__init__(node_name, name, age)
        #初始化要用的父类内容
        
        self.book = book

def main():
    rclpy.init()

    node = WriterNode('sb', 'sb', 91, 'shu')
#          对应父类的node_name, name, age, 对应子类的book
    
    node.eat('shi')

    rclpy.spin(node)
    node.destroy_node()  #返还系统资源
    rclpy.shutdown()

if __name__ == '__main__':
    main()#一般都有
