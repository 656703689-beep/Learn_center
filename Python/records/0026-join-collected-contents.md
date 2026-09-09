# Join collected AI contents into final text

用户已掌握用 `final_text = "\n".join(contents)` 把收集到的多条 AI 回复合并成一段文本。这个理解把“列表保存中间结果”推进到“字符串作为最终回答”，并且用户能识别 `join()` 前面的字符串就是插入到每两项之间的分隔符。

**Evidence** — 用户正确预测 `"\n".join(contents)` 会输出三行文本，亲手运行 `final_text.py` 得到 `先检查输入`、`再检查条件`、`最后整理回答` 三行；随后把分隔符迁移为中文逗号 `，`，先修正了空格细节，再运行得到 `先检查输入，再检查条件，最后整理回答`。
