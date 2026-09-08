# 掌握从多份报告生成总体 summary dict

用户已经能把多份单组报告 `report` 汇总成总体报告 `summary`，并理解 `summary["total_groups"]` 与 `summary["passed_groups"]` 分别表示总组数和通过组数。这说明用户能从多条结构化数据生成更高一层的结构化汇总。

## Evidence

- 能预测循环三份报告时，通过组数为 `2`。
- 曾把 `summary["passed_groups"]` 误判为 `1`，随后理解题目中 `passed_count = 2` 已经给定，因此 `summary["passed_groups"]` 是 `2`。
- 编写并运行 `summary_report.py`，通过 `build_summary(reports)` 返回 `{"total_groups": 3, "passed_groups": 2}`。
- 能区分单个 `report` 描述一组，总体 `summary` 描述全部组。
- 迁移时把第二组改成 `[35, 30, 20]`，能先预测再运行得到 `{"total_groups": 3, "passed_groups": 3}`，并输出总组数 `3`、通过组数 `3`。

## Implications

下一课可以开始引入 `json`：把 Python 的 `dict` / `list` 转成 JSON 字符串。建议只讲 `import json` 和 `json.dumps(data, ensure_ascii=False)`，直接连接 AI API 常见的数据交换格式。
