# demo_python_topic · 本包阅读顺序

| 序 | 文件 | 看什么 |
| --- | --- | --- |
| 1 | [`novel_pub_node.py`](demo_python_topic/novel_pub_node.py) | 发布者：`create_publisher(String, 'novel', 10)`、`create_timer(5, cb)`、`Queue` 按行入队 |
| 2 | [`novel_sub_node.py`](demo_python_topic/novel_sub_node.py) | 订阅者：`create_subscription(String, 'novel', cb, 10)`、回调里取 `msg.data` |
| — | [`setup.py`](setup.py) | 入口只注册了发布者（订阅者还没收尾） |

> 文件名保持原样是有意的：ROS 的模块导入靠文件名，加数字/逗号前缀会让 `ros2 run` 报错。
> 顺序用本页和根目录的 [`REVIEW.md`](../../../../REVIEW.md) 表达。

## 跑起来

```bash
cd ../..                        # 回到 topic_ws
colcon build --symlink-install
source install/setup.bash
ros2 run demo_python_topic novel_pub_node
ros2 topic echo /novel          # 另一个终端
```
