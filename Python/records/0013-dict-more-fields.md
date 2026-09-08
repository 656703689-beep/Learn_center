# 掌握给 dict 报告增加更多字段

用户已经能在报告 `dict` 中同时保存总次数、偏小次数、偏大次数、猜中次数和总结，并能通过 key 读取对应 value。这说明用户对结构化数据的理解从“单个字段取值”推进到“多个统计字段组合成一份报告”。

## Evidence

- 能预测多字段 `dict` 中 `report["small"]`、`report["big"]`、`report["hits"]` 的输出分别为 `2`、`2`、`1`。
- 编写并运行 `dict_fields.py`，通过 `build_report(results)` 返回包含 `"total"`、`"small"`、`"big"`、`"hits"`、`"summary"` 的字典。
- 第一轮输入 `[10, 20, 40, 30]` 后，得到偏小次数 `2`、偏大次数 `1`、猜中次数 `1`，总结为“已经猜中过，测试通过”。
- 迁移输入 `[35, 40, 20]` 后，能先正确预测再运行得到：
  - `report["small"]` 为 `1`
  - `report["big"]` 为 `2`
  - `report["hits"]` 为 `0`
  - `report["summary"]` 为 `整体偏大，可以试小一点`

## Implications

下一课可以开始引入嵌套数据或多个报告组成的列表：例如 `reports = [report1, report2]`，让用户理解“列表里放 dict”。这是后续理解 AI API 返回结果中常见结构（外层 list、内层 dict）的自然下一步。
