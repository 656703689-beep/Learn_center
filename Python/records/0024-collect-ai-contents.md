# 掌握把多条 content 收集进列表

用户已经能从逐条打印 AI 回复，过渡到把每条 `message["content"]` 保存进 `contents` 列表。这说明用户能区分 `print()` 的显示作用和 `append()` 的保存作用，并能把第六课的列表收集模式迁移到当前 AI 返回结构。

## Evidence

- 能正确预测两份 `choices` 的循环会输出：
  - `第一步检查输入`
  - `第二步检查条件`
- 曾把第一轮后的 `contents` 误答成两条都已收集，随后修正为：
  - `["第一步检查输入"]`
  说明开始区分“当前轮结束”和“全部循环结束”。
- 能正确预测全部循环结束后，`print(contents)` 会输出：
  - `['第一步检查输入', '第二步检查条件']`
- 亲手新建并运行 `collected_contents.py`，先遇到：
  - `NameError: name 'content' is not defined`
  随后补上：
  - `content = message["content"]`
  并成功输出：
  - `['第一步检查输入', '第二步检查条件']`
- 能把 `response_text` 迁移为三份回复，循环中继续使用 `contents.append(content)`，并正确预测和运行得到：
  - `['先检查输入', '再检查条件', '最后整理回答']`

## Implications

下一课可以继续使用收集到的 `contents` 列表做后续处理，例如用 `len(contents)` 统计回复条数，或把多条文字合并成一段总结。
