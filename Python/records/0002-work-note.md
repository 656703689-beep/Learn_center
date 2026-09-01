# 工作备注：Python 第 2 次学习

日期：2026-09-01

本次工作围绕 `while` 条件循环展开，把第一天只能判断一次的猜数字程序升级为可持续接收输入、直到猜中才结束，并记录猜测次数。

## 本次完成内容

- 创建第二课 `lessons/0002-repeat-until-right.html`，包含旧知识回忆、循环模型、代码实作、状态追踪、排错与复盘。
- 创建 `reference/python-while-loop.html`，整理 `while` 的基本结构、状态更新、缩进和常见错误。
- 为第一课和原有速查页补充第二课导航入口。
- 在 `RESOURCES.md` 中补充 Python 3.13 官方 `while` 教程与语言参考。
- 将 `study_log.py` 的单次猜数字判断升级为条件循环，并加入 `attempts` 计数器。
- 更新测试，使其验证猜小或猜大后程序继续接收输入，并在猜中时正确退出和显示次数。
- 写入 `records/0002-while-condition-and-state.md`，保存本次掌握证据。

## 本次掌握内容

- `while` 会在每轮开始前检查条件；条件为 `True` 时执行循环体，为 `False` 时退出。
- `guess != secret` 表示“尚未猜中”，比 `guess < secret` 更符合“直到相等才停止”的目标。
- 循环体必须更新条件依赖的状态，否则程序可能无法正常停止。
- `attempts = attempts + 1` 会读取旧值、加一并写回；`attempts = attempts` 不会改变计数。
- 缩进决定一行代码是在每轮执行，还是在循环结束后执行。

## 典型错误与修正

1. 循环条件最初写成 `while guess < secret:`，导致猜大时也退出循环。

   修正为：

   ```python
   while guess != secret:
   ```

2. 计数器最初写成 `attempts = attempts`，因此结果始终为零。

   修正为：

   ```python
   attempts = attempts + 1
   ```

## 验证结果

- 实际运行时，程序能在猜小和猜大后继续，并只在输入秘密数字 `7` 后退出。
- 一次实际练习正确记录了共 `15` 次猜测。
- `python -m unittest discover -s tests -v`：3 项测试全部通过。
- 第二课与循环速查页已检查桌面和窄屏布局、折叠答案、内部链接及浏览器控制台。

## 下次建议

先用两分钟凭记忆重写一个最小 `while` 循环，再比较“次数未知时使用 `while`”与“次数已知时使用 `for` 和 `range()`”。
