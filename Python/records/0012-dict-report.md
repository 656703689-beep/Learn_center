# 掌握用 dict 保存带名字的报告数据

用户已经能用 `dict` 把报告从一整句字符串整理成带名字的数据，并能用 key 取出对应 value。这说明用户开始掌握 Python 中结构化数据的基本形状，为后续理解 JSON 和 AI API 返回结果打基础。

## Evidence

- 能预测 `report["hits"]` 会输出 `1`，理解 key `"hits"` 对应 value `1`。
- 能预测 `report["total"]`、`report["hits"]`、`report["summary"]` 三行输出分别是 `4`、`0` 和 `这组测试里没有猜中`。
- 编写并运行 `dict_report.py`，通过 `build_report(results)` 返回：
  - `"total"`：总测试次数
  - `"hits"`：猜中次数
  - `"summary"`：总结文字
- 将输入迁移到 `[10, 20, 25, 28]` 后得到正确结果列表、正确 dict 和正确三行字段输出：
  - `total` 为 `4`
  - `hits` 为 `0`
  - `summary` 为 `这组测试里没有猜中`

## Implications

下一课可以继续在 `dict` 上做小步迁移：从“读取已有 key”进入“新增或修改 key”，例如给报告增加 `"small"` 和 `"big"` 两个字段。教学时继续强调：`list` 保存一串结果，`dict` 保存带名字的数据；方括号在 `dict` 里表示按 key 取值，不是按位置取值。
