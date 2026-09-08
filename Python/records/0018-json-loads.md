# 掌握用 json.loads 把 JSON 字符串转回 Python 数据

用户已经能用 `json.loads(json_text)` 把 JSON 字符串转回 Python 的 `dict` 或 `list`，并继续按 key 取值或用 `for` 循环处理。这说明用户已经掌握 JSON 双向转换的基础方向。

## Evidence

- 能回忆 `json.dumps(summary, ensure_ascii=False)` 会把 Python `dict` 转成 JSON 字符串，并注意到默认逗号后有空格。
- 曾把 `print(summary["total_groups"])` 误判成打印一个小 `dict`；随后理解 `summary["total_groups"]` 取出的是数字 value。
- 编写并运行 `json_read.py`，用 `json.loads(json_text)` 把 JSON 字符串转回 Python `dict`，并正确输出组名、猜中次数和总结。
- 迁移到 JSON 列表字符串后，能先预测再运行得到：
  - `第一组`
  - `1`
  - `第二组`
  - `0`
- 能理解 `reports = json.loads(json_text)` 后，`reports` 是 Python `list`，循环里的 `report` 是一份 `dict`。

## Implications

下一课可以进入“模拟 AI API 响应”：把一段 JSON 字符串当作外部系统返回的数据，用 `json.loads()` 解析后读取 `message` 或 `reply` 字段。教学时继续强调：外部系统给的是文本，Python 要先解析成数据，才能按 key 读取。
