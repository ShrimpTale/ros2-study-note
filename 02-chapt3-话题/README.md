# 第 3 章 · 话题（发布 / 订阅）

先抄模板，再写发布者，最后写订阅者。发布者从网上抓小说、按行塞进队列、定时发出去；订阅者收下来再塞进自己的队列。

## 文件

| 文件 | 学到的东西 |
| --- | --- |
| `muban.py` | 空模板：只有 `Node` 子类 + `main()`，用来开新话题节点时复制 |
| `topic_ws/src/demo_python_topic/.../novel_pub_node.py` | `create_publisher(String, 'novel', 10)` 三个参数（消息类型 / 话题名 / 缓存）；`create_timer(5, cb)` 两个参数（间隔秒数 / 回调）；`Queue` 先建再往里放；`text.splitlines()` 是普通 Python 字符串方法，不是 ROS 消息 |
| `topic_ws/src/demo_python_topic/.../novel_sub_node.py` | `create_subscription(String, 'novel', cb, 10)` 四个参数；回调签名 `(self, msg)`，`msg.data` 才是内容 |

## 构建与运行

```bash
cd topic_ws
colcon build --symlink-install
source install/setup.bash

# 终端 A
ros2 run demo_python_topic novel_pub_node
# 终端 B
ros2 run demo_python_topic novel_sub_node
# 终端 C
ros2 topic echo /novel
```

`novel_pub_node.py` 的 `download(url)` 要传小说地址（`main()` 里那句 `node.download()` 还没补参数）。

## 还没做完的地方

`novel_sub_node.py` 停在半成品：

- 第 14 行写的是 `create_subscription(..., novel_callback, 10)`，`novel_callback` 这个全局名不存在，运行会 `NameError`，应该是 `self.novel_callback`；
- 文件末尾只有 `def main()`，没有 `if __name__ == '__main__': main()`；
- 开头 `import espeakng` 是打算做语音播报的，还没接上。

## 踩过的坑

- `package.xml` 里 `<depend>example_interfances</depend>` 拼错了（少了 `e`，应为 `example_interfaces`），`rosdep` 会找不到依赖，但包本身能编过——所以一直没发现。
- 订阅者回调里 `msg` 是消息对象，不是字符串；要先 `msg.data` 再入队，否则队列里存的是对象，后面取出来用会不对。
