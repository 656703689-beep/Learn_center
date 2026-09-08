# 掌握逐条读取 choices 里的多份回复

用户已经能用 `for choice in response["choices"]` 逐份读取 AI 返回结构里的多条回复，并从每份 `choice` 中继续取出 `message["content"]`。

## Evidence

- 能正确预测上一课结构中：
  - `response["choices"][0]["message"]["content"]` 输出 `先检查输入`
- 能正确预测两份 `choices` 的循环输出：
  - `先检查输入`
  - `再核对结果`
- 能说出第一轮 `choice` 是当前列表里的第一份字典：
  - `{"message": {"content": "先检查输入"}}`
- 亲手编写并运行 `all_choices.py`，先遇到：
  - `NameError: name 'choices' is not defined`
  随后补上：
  - `choices = response["choices"]`
  并成功输出两份回复：
  - `可以先检查输入`
  - `也可以核对输出`
- 能把 `response_text` 迁移为三份回复，循环代码保持不变，并正确预测和运行得到：
  - `先打印输入`
  - `再检查条件`
  - `最后核对结果`

## Implications

下一课可以继续靠近真实 AI API 的返回结构：在逐条读取 `choices` 的基础上，加入每条回复里的 `role` 字段，练习同时读取 `role` 和 `content`，并继续巩固“列表负责多份，字典负责字段名”。
