# 掌握在 choices 循环中读取 role 和 content

用户已经能在 `for choice in response["choices"]` 的每一轮里读取当前 `message` 字典中的多个字段：`role` 和 `content`。这说明用户开始把“循环负责换到下一条”和“key 负责读取当前条里的字段”分开理解。

## Evidence

- 能正确预测上一课循环会输出：
  - `先打印输入`
  - `再检查条件`
- 曾把 `message["role"]` 误答成同时包含 `assistant content 先打印输入`，随后修正为只输出：
  - `assistant`
  说明已经开始区分同一层里不同 key 各自读取自己的 value。
- 能正确预测两份数据、每份打印 `role` 和 `content` 时会输出四行：
  - `assistant`
  - `先打印输入`
  - `assistant`
  - `再检查条件`
- 亲手改造并运行 `all_choices.py`，在同一轮里执行：
  - `print("角色：", message["role"])`
  - `print("内容：", message["content"])`
  并成功输出两份回复的角色和内容。
- 能把 `response_text` 迁移为三份回复，循环代码保持不变，并正确预测和运行得到：
  - `角色： assistant`
  - `内容： 第一步检查输入`
  - `角色： assistant`
  - `内容： 第二步检查条件`
  - `角色： assistant`
  - `内容： 最后整理回答`

## Implications

下一课可以继续靠近真实 AI 程序的数据流：把读取到的多条 `content` 收集进一个列表，练习从“逐条打印”过渡到“保存结果供后续处理”。
