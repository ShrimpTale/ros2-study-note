# 自用复习笔记，所有内容为ai协助整理

其实这些完全可以放在本地的，但是我寻思这里太空了要放点什么

因为记得确实详细所以也许有某些参考价值（？）

复习入口：[`REVIEW.md`](REVIEW.md)

笔记基于 B站鱼香ROS机器人 《ROS 2机器人开发从入门到实践》

下面都是ai实时更新的概览

## 环境

| 项 | 版本 |
| --- | --- |
| OS | Ubuntu 22.04 |
| ROS 2 | Humble |
| Python | 3.10 |
| 构建 | colcon（`ament_python` 包） |

## 目录结构

```text
.
├── REVIEW.md                          # 复习路线：1 → 8 步，要点 + 自测
├── 01-chapt2-节点基础/                 # 第 2 章（第 1–5 步）
│   ├── README.md                     # 本章说明 + 踩过的坑
│   ├── ros2_python_node.py           # 最早的散装练习（带 __main__）
│   └── chapt2_ws/src/demo_python_pkg/
│       ├── README.md                 # 本包内阅读顺序
│       ├── demo_python_pkg/          # python_node / person_node / writer_node / learn_thread
│       ├── package.xml
│       ├── setup.py                  # entry_points 在这里
│       └── test/                     # ament 模板自带的三件套
└── 02-chapt3-话题/                    # 第 3 章（第 6–8 步）
    ├── README.md
    ├── muban.py                      # 话题节点模板
    └── topic_ws/src/demo_python_topic/
        ├── README.md                 # 本包内阅读顺序
        ├── demo_python_topic/        # novel_pub_node / novel_sub_node
        ├── package.xml
        └── setup.py
```
## 已知问题（有意保留，当作笔记）

1. `novel_sub_node.py` 第 14 行传的是 `novel_callback`（全局名不存在），应该是 `self.novel_callback`；文件也没有 `if __name__ == '__main__': main()`，`espeakng` 导入了没用——这篇停在"还差最后一步"。
2. `person_node.py` 第 24 行 `self.get_logger().info("{self.name},{self.age}")` 少了 `f` 前缀，会原样打印。
3. `demo_python_topic/package.xml` 里 `<depend>example_interfances</depend>` 拼错了（应为 `example_interfaces`）。
4. 还写过一版 `writer_node_error.py`（`super().__init__(name, age, node_name)` 参数顺序反了），只在容器的 `install/` 里留着，没纳入仓库。

## License

各功能包内保留 ROS 2 包模板自带的 Apache-2.0 `LICENSE`。
