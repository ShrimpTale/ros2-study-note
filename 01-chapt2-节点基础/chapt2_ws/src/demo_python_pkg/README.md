# demo_python_pkg · 本包阅读顺序

| 序 | 文件 | 看什么 |
| --- | --- | --- |
| 1 | [`python_node.py`](demo_python_pkg/python_node.py) | 最小节点搬进包；入口不在文件里，在 `setup.py` 的 `console_scripts` |
| 2 | [`person_node.py`](demo_python_pkg/person_node.py) | 继承 `Node` 写自定义类：`__init__`、`super().__init__()`、成员属性 |
| 3 | [`writer_node.py`](demo_python_pkg/writer_node.py) | 再继承一层：父类参数按序透传，再加自己的 |
| 4 | [`learn_thread.py`](demo_python_pkg/learn_thread.py) | `threading` + `requests`：为什么下载要另开线程 |
| — | [`setup.py`](setup.py) | `entry_points` 注册可执行文件（那两行注释就是坑的记录） |

> 文件名保持原样是有意的：ROS 的模块导入靠文件名（`demo_python_pkg.python_node`），
> 加 `1,`、`2,` 这种前缀会让 `ros2 run` 报 `SyntaxError`。顺序用本页和根目录的
> [`REVIEW.md`](../../../../REVIEW.md) 表达。

## 跑起来

```bash
cd ../..                        # 回到 chapt2_ws
colcon build --symlink-install
source install/setup.bash
ros2 run demo_python_pkg python_node     # person_node / writer_node / learn_thread 同理
```
