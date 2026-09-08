# 掌握读取 choices 列表里的 AI 回复

用户已经能读取更接近真实 AI API 的返回结构：外层 `dict` 里有 `choices` 列表，列表第一个元素里再嵌套 `message` 字典，最终读取 `content` 字段。

## Evidence

- 能正确预测：
  - `response["choices"][0]["message"]["content"]` 输出 `整体偏大，可以试小一点`
  - `response["model"]` 输出 `demo`
- 亲手编写并运行 `choices_response.py`，从 JSON 字符串：
  - `{"choices": [{"message": {"role": "assistant", "content": "第一组通过，第二组继续测试"}}], "usage": {"total_tokens": 156}}`
  解析出 Python 数据，并正确输出：
  - `角色： assistant`
  - `内容： 第一组通过，第二组继续测试`
  - `token数量： 156`
- 能把 `response_text` 迁移成：
  - `{"choices": [{"message": {"role": "assistant", "content": "三组都通过，可以进入下一课"}}], "usage": {"total_tokens": 88}}`
  并得到正确内容：
  - `角色： assistant`
  - `内容： 三组都通过，可以进入下一课`
  - `token数量： 88`

## Implications

下一课可以进入“读取 choices 列表里的多条回复”：用 `for choice in response["choices"]` 循环处理多条 AI 回复。教学重点应放在把已经学过的 `for` 循环与当前的嵌套结构结合起来。
