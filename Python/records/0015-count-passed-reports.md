# 掌握统计多份报告里的通过组数

用户已经能循环 `reports` 列表，逐份读取报告字典里的 `report["hits"]`，并在 `hits > 0` 时累计通过组数。这说明用户能把 `for`、`if`、`dict` 取值和计数器组合起来处理多份结构化数据。

## Evidence

- 能预测 `reports` 中三份报告的通过组数为 `2`：A组和 C组 的 `hits` 都大于 `0`。
- 编写并运行 `passed_reports.py`，先生成三份报告，再用 `passed_count = 0` 和循环统计通过组数。
- 第一轮输入中，只有第一组 `hits = 1`，第二组和第三组 `hits = 0`，最终输出 `通过组数： 1`。
- 迁移时把第三组改成 `[10, 30, 25, 28]`，能先预测再运行得到第三组 `hits = 1`，最终输出 `通过组数： 2`。

## Implications

下一课可以把“通过组数”和“总组数”合成一个总体报告，例如 `summary = {"total_groups": len(reports), "passed_groups": passed_count}`。这会自然引出“从多份数据生成汇总 dict”，接近真实 AI 应用中对多条结果做汇总的模式。
