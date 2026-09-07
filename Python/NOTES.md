# 教学备忘

## 用户与环境

- 长期目标：AI
- 当前阶段：第一次正式 Python 学习
- 教学语言：中文；代码与 Python 术语保留英文
- Windows 环境已安装 Python 3.13.14
- 可用启动命令：`python`；`py` 启动器当前不可用

## 第一课范围

- 用户提供的课程提纲包含：环境、变量、类型、`input()`、`print()`、缩进规则
- 练习路线包含：温度换算、BMI 计算、猜数字，以及记录一次报错与修复
- 为控制认知负担，第一课用同一条“输入 → 处理 → 输出”数据流串起这些内容，并分检查点完成

## 进度

- 2026-09-01：已确认使命为“用 Python 进入 AI”。
- 2026-09-01：用户已用运行结果证明掌握第一课核心内容；证据保存在 `records/0001-python-first-study.md`。
- 2026-09-01：完成第二次学习，掌握 `while` 的条件检查、状态更新和退出；程序能反复猜到正确并统计次数。
- 第二课掌握证据保存在 `records/0002-while-condition-and-state.md`：用户修正了停止条件与计数器错误，并能解释为什么输入 `7` 后循环结束。
- 2026-09-03：用户已把第三课知识应用到 `guess_number.py`：用 `range(1, max_attempts + 1)` 管理 8 次机会，用 `break` 在猜中时提前停止，并能显示剩余次数。猜中路径与机会耗尽路径均已实际运行验证；证据保存在 `records/0003-for-range-boundary-and-early-stop.md`。
- 2026-09-03：已完成第四次学习，掌握函数的数据流：定义、参数、实参、调用与 `return`。用户完成 `function_lab.py` 并通过三条分支验证，还能在新例子中准确识别参数 `number`、实参 `6` 和返回结果 `12`；证据保存在 `records/0004-function-parameters-and-return.md`。
- 2026-09-05：已完成第五次学习，掌握列表保存多个值、`for` 按顺序逐个取元素、每轮调用已学函数。用户亲手编写并运行 `batch_guesses.py`，能预测列表顺序变化、能区分 `print(guess)` 与 `print(result)`，并能把 `[10, 30, 40, 25]` 批量传给 `compare_guess(guess, secret)` 得到正确四行输出；证据保存在 `records/0005-list-batch-check.md`。
- 2026-09-06：已完成第六次学习，掌握用空列表和 `append()` 收集每轮处理结果。用户亲手编写并运行 `collect_results.py`，把 `compare_guess()` 的返回值收集到 `results` 列表；还能修正把整个 `guesses` 传给函数的错误，并在迁移输入 `[30, 31, 29]` 后得到正确结果。证据保存在 `records/0006-collect-results-with-append.md`。
- 2026-09-06：已完成第七次学习，掌握用 `count()` 统计列表中某个结果出现几次。用户亲手编写并运行 `count_results.py`，先用 `append()` 收集 `results`，再统计“太小了/太大了/猜中了”的次数；还能修正 `result` 与 `results` 混淆，并在迁移输入 `[30, 31, 29, 30]` 后得到正确统计。证据保存在 `records/0007-count-results.md`。
- 2026-09-06：已完成第八次学习，掌握把 `count()` 得到的次数交给 `if`，输出一句测试总结。用户亲手编写并运行 `summarize_results.py`，先收集结果，再统计 `hit_count`，最后判断是否猜中过；还能把输入迁移到 `[10, 20, 25]` 并得到“没有猜中”的正确总结。证据保存在 `records/0008-summarize-with-if.md`。
- 2026-09-07：已完成第九次学习，掌握用 `if/elif/else` 根据多个统计数字输出建议。用户亲手实现并运行建议逻辑，能根据 `small_count`、`big_count`、`hit_count` 判断整体偏小、整体偏大或已经猜中过；还修正了 `bug_count` 与 `big_count` 的变量名错误，并在迁移输入 `[35, 40, 20]` 后得到正确建议。证据保存在 `records/0009-suggest-with-elif.md`。
- 2026-09-07：已完成第十次学习，掌握让函数接收整个 `results` 列表，并 `return` 一句总结。用户亲手编写并运行 `summary_function.py`，通过 `summary = suggest_from_results(results)` 获取总结；还能修正“参数接到 if 判断”的误解，理解参数接收的是调用时传入的整个列表。证据保存在 `records/0010-function-takes-list.md`。
- 2026-09-07：已完成第十一次学习，掌握用 `len()` 得到列表长度，并结合 `count()` 生成“共测试几次、猜中几次”的报告。用户亲手编写并运行 `report_results.py`，实现 `build_report(results)`；还能修正结果列表里误放列表本身的问题，并在迁移输入 `[10, 20, 25, 28]` 后得到正确报告。证据保存在 `records/0011-report-with-len.md`。
- 2026-09-07：已完成第十二次学习，掌握用 `dict` 保存带名字的报告数据，并用 key 取出 value。用户亲手编写并运行 `dict_report.py`，实现 `build_report(results)` 返回包含 `"total"`、`"hits"`、`"summary"` 的字典；还能把输入迁移到 `[10, 20, 25, 28]`，得到正确的结果列表、报告字典和字段输出。证据保存在 `records/0012-dict-report.md`。
- 2026-09-07：第十三次学习已开启，主题为给报告 `dict` 增加 `"small"` 和 `"big"` 字段。目标：让报告同时保存总次数、偏小次数、偏大次数、猜中次数和总结。课件保存在 `lessons/0013-dict-more-fields.html`，速查保存在 `reference/python-dict-fields.html`。

## 后续教学要点

- 第四课中，用户曾把分支条件与返回值的来源混淆，也曾需要逐项拆解 `def` 那一行；第五课已通过 `result = compare_guess(guess, secret)` 继续巩固“函数返回文字，再由 `print(result)` 显示”的数据流。
- 聊天教学延续一题一反馈；第十三课重点是把 `small_count`、`big_count`、`hit_count` 放进同一个报告字典。继续强调字段名与变量名的对应关系，避免把 `"small"`、`"big"` 与中文返回值 `"太小了"`、`"太大了"` 混淆。
