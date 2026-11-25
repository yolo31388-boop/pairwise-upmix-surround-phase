# pairwise-upmix-surround-phase

## 领域

游戏、图形与多媒体

## 主题

立体声上混环绕声

## 说明

自适应中置提取、按时间延迟换算、延迟线重建。

初始状态下 `av/upmix_surround.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
