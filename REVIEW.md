# 复习路线（1 → 8）

按顺序走，每步只看一个文件：先读注释，再对着代码看一遍，最后回答文末的自测题。
标题链接直接跳到 GitHub 上对应的行，不用在目录里翻。

预计用时：40 分钟（第 1–5 步约 25 分钟，第 6–8 步约 15 分钟）。

目录前的 `01-` / `02-` 只用来排序，包内文件名没动（ROS 导入依赖原名）；点标题会跳到 GitHub 对应的行。

---

## 第 1 步 · 一个节点最小能有多小

[`01-chapt2-节点基础/ros2_python_node.py` L7–L21](01-chapt2-节点基础/ros2_python_node.py#L7-L21) · 21 行 · 2026-10-20

**目标**：记住 `init → Node → spin → shutdown` 这个顺序。

要点：

- `rclpy.init()` 初始化上下文、分配资源；`rclpy.shutdown()` 收尾。
- `Node('python_node')` 是**手动**创建的，ROS 2 里没有 ROS 1 那种隐式节点；`python_node` 就是 `ros2 node list` 里看到的名字。
- `rclpy.spin(node)` 是阻塞循环，一直转，直到 Ctrl-C 才返回——所以它后面的 `shutdown()` 是"退出时才执行"。

自测：为什么 `spin(node)` 之后的代码在运行时看起来"没执行"？

---

## 第 2 步 · 把节点搬进功能包

[`.../demo_python_pkg/python_node.py` L7–L19](01-chapt2-节点基础/chapt2_ws/src/demo_python_pkg/demo_python_pkg/python_node.py#L7-L19) · 22 行 · 2026-10-22

配套看：[`setup.py` L21–L29](01-chapt2-节点基础/chapt2_ws/src/demo_python_pkg/setup.py#L21-L29)（`entry_points` 那段）

**目标**：搞清楚 `ros2 run` 到底跑了哪个函数。

要点：

- 这个文件里没有 `if __name__ == '__main__'`——入口不在这里，在 `setup.py`：
  `'python_node = demo_python_pkg.python_node:main'` 意思是"可执行名 = 包.模块:函数"。
- `ros2 run demo_python_pkg python_node` → 实际执行 `demo_python_pkg/python_node.py` 里的 `main()`。
- 注释里那句"记得结尾加逗号"是踩过坑的：两条 entry 之间漏逗号，Python 会把两个字符串**隐式拼接**，装出一个畸形脚本（`...mainexe`）。

自测：如果 `main` 改名成 `run`，要改哪一行？

---

## 第 3 步 · 写一个自定义节点类

[`.../person_node.py` L8–L26](01-chapt2-节点基础/chapt2_ws/src/demo_python_pkg/demo_python_pkg/person_node.py#L8-L26) · 40 行 · 2026-10-22（10-26 补的注释）

**目标**：`class XxxNode(Node)` 的骨架。

要点：

- `__init__` 里第一件事是 `super().__init__(node_name)`：父类负责把节点注册进 ROS，不调它，后面 `create_publisher` 之类全用不了。
- 参数带类型注解：`(self, node_name: str, name_value: str, age_value: int) -> None`，`-> None` 表示不返回值。
- 自己的属性 `self.name` / `self.age` 在 `__init__` 里建；方法（`eat`）里用 `self.get_logger().info()` 打日志，会带节点名。

自测：`self.name` 和局部变量 `name` 有什么区别？为什么函数外不能 `self.name = ...`？

---

## 第 4 步 · 再继承一层

[`.../writer_node.py` L5–L10](01-chapt2-节点基础/chapt2_ws/src/demo_python_pkg/demo_python_pkg/writer_node.py#L5-L10) · 24 行 · 2026-10-22

**目标**：子类怎么把父类的参数接过来。

要点：

- `WriterNode(PersonNode)`：父类已经是 `Node` 的子类，所以这里**不用再** `from rclpy.node import Node`。
- `super().__init__(node_name, name, age)` 必须按父类的参数顺序传，传完再写自己的 `self.book = book`。
- `main()` 里 `destroy_node()` 返还资源，再 `shutdown()`。

自测：`WriterNode('sb','sb',91,'shu')` 四个参数分别落到父类和子类的哪个属性上？

---

## 第 5 步 · 线程：为什么不能直接调下载

[`.../learn_thread.py` L15–L24](01-chapt2-节点基础/chapt2_ws/src/demo_python_pkg/demo_python_pkg/learn_thread.py#L15-L24) · 37 行 · 2026-10-26

**目标**：`threading.Thread(target=..., args=...)` 两个参数。

要点：

- `target` 是要执行的函数，`args` 是传给它的参数元组——注释里用两个箭头标出来了。
- 如果在 `start_download` 里直接 `self.download(...)`，三个下载会串行，一个卡住全卡住；`Thread(...).start()` 才是并发。
- `requests.get()` 返回 `Response` 对象，`.text` 是它的**属性**（不是 `requests` 的方法）；`encoding='utf-8'` 决定怎么解码。

自测：`thread.start()` 之后 `start_download` 会等下载完吗？打印出来的线程号为什么不同？

---

## 第 6 步 · 话题节点模板

[`02-chapt3-话题/muban.py` L4–L13](02-chapt3-话题/muban.py#L4-L13) · 13 行 · 2026-10-26

**目标**：开新话题节点时复制它。

要点：

- 骨架只有 `class XxxNode(Node)` + `__init__` + `main`，没有发布也没有订阅。
- 复制后改三处：类名、`main()` 里的节点名、`super().__init__(node_name)` 之前的参数。

自测：要在这个模板上加一个发布者，最少加几行？加在哪？

---

## 第 7 步 · 发布者：队列 + 定时器

[`.../novel_pub_node.py` L9–L45](02-chapt3-话题/topic_ws/src/demo_python_topic/demo_python_topic/novel_pub_node.py#L9-L45) · 62 行 · 2026-10-29

**目标**：`create_publisher` / `create_timer` 的参数，以及"先入队、定时再发"的套路。

要点：

- `self.create_publisher(String, 'novel', 10)`：消息类型、话题名、**缓存大小**（不是队列长度）。
- `self.create_timer(5, self.timer_callback)`：间隔秒数、回调函数。
- `download()` 里 `requests.get` → `encoding='utf-8'` → `text.splitlines()` 按行切 → 每行 `put` 进 `Queue`；`timer_callback` 每次取一行，包成 `String()`，赋给 `msg.data` 再 `publish`。
- `splitlines()` 是普通字符串方法，跟 ROS 消息无关——注释里专门标了"不是 ros 的消息类型"。

自测：为什么队列要在 `create_timer` **之前**建？

---

## 第 8 步 · 订阅者：回调里拿到的是什么

[`.../novel_sub_node.py` L8–L29](02-chapt3-话题/topic_ws/src/demo_python_topic/demo_python_topic/novel_sub_node.py#L8-L29) · 29 行 · 2026-10-29（未完成）

**目标**：`create_subscription` 四个参数 + 回调签名。

要点：

- `self.create_subscription(String, 'novel', callback, 10)`：消息类型、话题名、回调、缓存。
- 回调是 `def novel_callback(self, msg)`：`msg` 是消息对象，内容在 `msg.data`，所以要 `put(msg.data)` 而不是 `put(msg)`。
- 模板还差最后三步没做完（注释里也记了）：`novel_callback` 少了 `self.`、没有 `__main__` 调用、`espeakng` 导入没用上。

自测：把 `msg` 直接放进队列，后面取出来用会出什么问题？

---

## 三个骨架（复习完扫一眼）

```python
# 最小节点
rclpy.init()
node = Node('python_node')
rclpy.spin(node)
rclpy.shutdown()
```

```python
# 发布者
self.pub = self.create_publisher(String, 'novel', 10)      # 类型 / 话题 / 缓存
self.create_timer(5, self.timer_callback)                  # 秒数 / 回调
msg = String(); msg.data = line; self.pub.publish(msg)
```

```python
# 订阅者
self.sub = self.create_subscription(String, 'novel', self.cb, 10)  # 类型 / 话题 / 回调 / 缓存
def cb(self, msg):
    self.queue.put(msg.data)                                # msg.data 才是内容
```

## 复习检查表

- [ ] 不看书能写出最小节点的四行
- [ ] 说清 `create_publisher` / `create_subscription` / `create_timer` 每个参数是什么
- [ ] 说清 `setup.py` 里 `console_scripts` 那一行的 `:` 两边分别是什么
- [ ] 说清为什么下载要另开线程、`target` 和 `args` 各放什么
- [ ] 说清 `super().__init__(...)` 不做会怎样
- [ ] 说清 `package.xml` 注释写在 `<?xml ?>` 前面为什么会让 colcon 装错包

## 按需回看

- 两个坑的来龙去脉：[`01-chapt2-节点基础/README.md`](01-chapt2-节点基础/README.md#踩过的坑都已修好记在这里)
- 话题这章的问题：[`02-chapt3-话题/README.md`](02-chapt3-话题/README.md#还没做完的地方)
- 全部已知问题汇总：[`README.md`](README.md#已知问题有意保留当作笔记)
