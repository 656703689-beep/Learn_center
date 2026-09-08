# 掌握读取嵌套 AI 回复

用户已经能读取嵌套 JSON 解析后的内层字段，例如 `response["message"]["content"]` 和 `response["usage"]["total_tokens"]`。这说明用户开始理解更接近真实 AI API 的返回结构：外层 `dict` 里还可以包着内层 `dict`。

## Evidence

- 在预测题中曾误以为会输出 key 名字 `content:`，随后理解 `response["message"]["content"]` 输出的是 `content` 对应的 value。
- 亲手编写并运行 `nested_response.py`，从 JSON 字符串：
  - `{"message": {"role": "assistant", "content": "三组都通过，可以进入下一步"}, "usage": {"total_tokens": 128}}`
  解析出 Python `dict`，再通过中间变量读取内层字段，正确输出：
  - `角色： assistant`
  - `内容： 三组都通过，可以进入下一步`
  - `token数量： 128`
- 能把 `response_text` 迁移成：
  - `{"message": {"role": "assistant", "content": "第二组还没有通过"}, "usage": {"total_tokens": 96}}`
  并正确运行得到：
  - `角色： assistant`
  - `内容： 第二组还没有通过`
  - `token数量： 96`

## Implications

下一课可以进入“嵌套列表里的 dict”：模拟更接近真实 AI 返回的 `choices` 列表，例如 `response["choices"][0]["message"]["content"]`。教学重点应放在区分 `dict` 用 key 取值、`list` 用 index 取元素。
