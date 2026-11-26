import rclpy
#相当于1的rospy

from rclpy.node import Node
#ros2里node需要手动添加

def main():
    rclpy.init()#初始化，分配资源 
    node =Node('python_node')
#   变量    类   类的实例，节点名称
#创建一个名为 python_node 的 ROS 2 节点对象，并把这个对象赋值给 Python 变量 node
    
    node.get_logger().warn('ccb')
    #让节点读日志然后info输出信息
    #能直接区分谁发的消息，与ros1 launch文件的ns（命名空间）功能相同

    rclpy.spin(node)#让node这个节点循环
    rclpy.shutdown()#手动关闭收尾

#if __name__ == '__main__':
#    main()
#不需要主函数，去setup.py声明即可调用函数
