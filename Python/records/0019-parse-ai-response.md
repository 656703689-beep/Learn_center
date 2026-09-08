# 掌握读取模拟 AI 回复

用户已经能把模拟 AI API 返回的 JSON 字符串用 `json.loads()` 解析成 Python `dict`，再通过 key 读取回复文字和统计字段。这说明用户已经能理解最基础的 AI 数据返回流程：外部系统返回文本，Python 解析成数据，程序再读取字段。

## Evidence

- 能正确预测并回答：
  - `response["reply"]` 输出 `整体偏大，可以试小一点`
  - `response["small"]` 输出 `1`
  - `response["big"]` 输出 `2`
- 亲手编写并运行 `ai_response.py`，从 JSON 字符串：
  - `{"reply": "第一组通过，第二组需要继续测试", "passed_groups": 1, "total_groups": 2}`
  解析出 Python `dict`，并正确输出：
  - `AI回复： 第一组通过，第二组需要继续测试`
  - `通过组数： 1`
  - `总组数： 2`
- 能把 `response_text` 迁移成：
  - `{"reply": "三组都通过，可以进入下一步", "passed_groups": 3, "total_groups": 3}`
  并正确运行得到：
  - `AI回复： 三组都通过，可以进入下一步`
  - `通过组数： 3`
  - `总组数： 3`

## Implications

下一课可以进入“读取嵌套 AI 回复”：模拟更接近真实 API 的结构，例如 `response["message"]["content"]`。教学重点应放在区分外层 `dict` 和内层 `dict`，并继续保持一题一反馈。
