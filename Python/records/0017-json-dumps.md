# 掌握用 json.dumps 把 Python 数据转成 JSON 字符串

用户已经能用 `json.dumps(data, ensure_ascii=False)` 把 Python 的 `dict` 和 `list` 转成 JSON 字符串，并开始区分 Python 数据结构与 JSON 文本。这说明用户已经接触到 AI API 常见的数据交换格式。

## Evidence

- 能预测 `summary["total_groups"]` 和 `summary["passed_groups"]` 分别输出 `3` 和 `2`。
- 能预测 `json.dumps(report, ensure_ascii=False)` 会输出包含中文的 JSON 字符串：`{"name": "第一组", "summary": "已经猜中过，测试通过"}`。
- 编写并运行 `json_report.py`，先打印 Python `dict`，再打印 JSON 字符串，观察到：
  - Python `dict` 输出使用单引号
  - JSON 字符串内容使用双引号
- 迁移到 `reports` 列表时，曾把输出误判为两行单独的 dict；随后修正理解：因为转换的是整个外层 `list`，所以 JSON 输出保留 `[` 和 `]`。
- 最终正确运行得到：`[{"name": "第一组", "hits": 1}, {"name": "第二组", "hits": 0}]`。

## Implications

下一课可以继续 JSON 反方向：用 `json.loads(json_text)` 把 JSON 字符串转回 Python 数据。教学时重点区分 `dumps` 是 Python 数据到 JSON 字符串，`loads` 是 JSON 字符串到 Python 数据。
