# 掌握 list 里放多个 dict

用户已经能把多份报告 `dict` 放进一个 `list`，并用 `for report in reports` 逐份读取字段。这说明用户开始理解 AI API 返回结果中常见的“外层列表、内层字典”结构。

## Evidence

- 能预测 `reports = [{"name": "A组", "hits": 1}, {"name": "B组", "hits": 0}]` 循环输出 `A组`、`1`、`B组`、`0`。
- 编写并运行 `multi_reports.py`，通过 `build_report(name, guesses, secret)` 生成多份报告字典。
- 第一轮能正确输出第一组和第二组报告：
  - 第一组总次数 `3`，猜中次数 `1`，总结为“已经猜中过，测试通过”
  - 第二组总次数 `3`，猜中次数 `0`，总结为“整体偏大，可以试小一点”
- 迁移时新增第三组 `report3 = build_report("第三组", [10, 20, 25, 28], secret)`，并将 `reports` 改成 `[report1, report2, report3]`。
- 曾把第三组名称误写为“第二组”，随后能定位到 `build_report()` 的第一个实参并修正为“第三组”。
- 最终正确输出第三组：总次数 `4`，猜中次数 `0`，总结为“整体偏小，可以试大一点”。

## Implications

下一课可以继续在 `list of dicts` 上做一个小步：统计多份报告里有几组通过，例如循环 `reports`，读取每个 `report["hits"]`，用计数器累计通过组数。这会把 `for`、`if`、`dict` 读取和计数器重新组合起来。
