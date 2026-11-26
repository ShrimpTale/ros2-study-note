# 第 2 章 · 节点基础

这一章从"一个文件里裸写节点"开始，慢慢过渡到功能包、自定义节点类和线程。

## 文件

| 文件 | 学到的东西 |
| --- | --- |
| `ros2_python_node.py` | 最小节点：`rclpy.init()` → `Node('名字')` → `spin()` → `shutdown()`；`rclpy` 相当于 ROS 1 的 `rospy`，但 node 要手动 `from rclpy.node import Node` |
| `chapt2_ws/src/demo_python_pkg/.../python_node.py` | 同样的节点搬进包；不写 `__main__`，入口由 `setup.py` 的 `console_scripts` 指向 `main` |
| `.../person_node.py` | `class PersonNode(Node)`：属性在 `__init__` 里建，`super().__init__(node_name)` 把父类参数接上；注释里记了"函数里创建了新东西就要用 `__init__`" |
| `.../writer_node.py` | 二次继承：`WriterNode(PersonNode)`，父类参数按顺序透传再补自己的；`destroy_node()` 返还资源 |
| `.../learn_thread.py` | `threading.Thread(target=..., args=...)`；直接在 `start_download` 里调 `self.download()` 会把整个线程卡住，所以必须开新线程 |

注释里那些箭头图（`↓` 指到参数上）是当时为了记住每个参数"是干嘛的"画的。

## 构建与运行

```bash
cd chapt2_ws
colcon build --symlink-install
source install/setup.bash

ros2 run demo_python_pkg python_node
ros2 run demo_python_pkg person_node
ros2 run demo_python_pkg writer_node
ros2 run demo_python_pkg learn_thread     # 先在本机 8001 起 http.server
```

## 踩过的坑（都已修好，记在这里）

1. **`package.xml` 里把注释放到 `<?xml ?>` 前面** → 不是合法 XML → `catkin_pkg` 解析失败 → colcon 把它当"普通 Python 包"装，不生成 `hook/ament_prefix_path.*` → `source install/setup.bash` 之后 `AMENT_PREFIX_PATH` 不变 → 报 `Package 'demo_python_pkg' not found`。现在注释在声明之后，`package.xml` 能正常解析。
2. **`setup.py` 里 `entry_points` 两条字符串之间漏逗号** → Python 隐式拼接成一个畸形脚本 `exe =demo_python_pkg.python_node:mainexe`。注释里特意写了"记得结尾加逗号"。
3. `writer_node.py` 里 `super().__init__(name, age, node_name)` 一开始把参数顺序写反了（父类要的是 `node_name, name, age`），后来改对了——错误版本一度留在容器 `install/` 里。

## 小记

- `Python 3.10` + `rclpy`，`Node` 子类化是后面所有代码的骨架。
- 日志用 `self.get_logger().info()`，会带节点名，比 `print` 更容易分辨是谁在说话。
