# 第 2 课 · 结构化输出：让模型说"机器话"

> **AI Agent 开发 · 20 小时速通 · 2 / 10**
> 节奏：**30 分钟学**（§0–§2，§0 含热身）→ **80 分钟练**（§3，代码放 `01_API基础/`）→ **10 分钟复盘**（§4）。
> 主线按 **DeepSeek** 写（你选定的那家）；智谱 / Qwen 的差异收在 §2.5，换供应商时回来查。
> 仍然只用 `requests`，今天不装任何新东西。

---

## §0 开工准备 + 热身（15 分钟）

第 1 课的练习还没动笔，没关系——本课开头就是热身：先亲手把一次 API 调用跑通，再谈结构化。三个环境变量（新开终端要重设，想一劳永逸就写进 `~/.zshrc`）：

```bash
export LLM_BASE_URL="https://api.deepseek.com"
export LLM_MODEL="deepseek-v4-flash"      # 便宜，练手首选
export LLM_API_KEY="在这里粘贴你的 key"     # platform.deepseek.com/api_keys
```

连通性预检，这一行跑通今天的路就通了：

```bash
curl -s "$LLM_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "'"$LLM_MODEL"'", "messages": [{"role": "user", "content": "ping"}]}' \
  | head -c 400
```

返回里能看到 `"choices"` 字样就是通了；`401` 是 key 不对，回控制台检查。

### §0.1 热身：亲手发第一次请求（10 分钟）

新建 `01_API基础/ex1_minimal_call.py`，把骨架敲进去——这就是第 1 课任务 1 的速通版，现在把这笔账补上：

```python
# 01_API基础/ex1_minimal_call.py —— 起步骨架
import os
import json
import requests

resp = requests.post(
    f"{os.environ['LLM_BASE_URL']}/chat/completions",
    headers={"Authorization": f"Bearer {os.environ['LLM_API_KEY']}"},
    json={
        "model": os.environ["LLM_MODEL"],
        "messages": [{"role": "user", "content": "用一句话解释什么是 JSON"}],
    },
    timeout=60,
)
data = resp.json()
print(json.dumps(data, ensure_ascii=False, indent=2))
```

跑通后盯住两处，后面 70 分钟全靠它们：

1. `data["choices"][0]["message"]["content"]`——模型的回复正文。
2. `data["usage"]`——计费三件套。

哪个字段干什么忘了，回[第 1 课 §2.2 的响应解剖图](0001-llm-api-stateless-messages.md)扫一眼。

> 💡 **课前读什么**
> [DeepSeek 文档](https://api-docs.deepseek.com/)里的 **JSON Output** 指南（10 分钟）。§2 讲的每条规矩都出自这里——先读原文再听我讲，体感完全不同。

---

## §1 核心认知：模型说的永远是"话"，不是"数据"

> ◆ **本课唯一必须带走的东西**
>
> **`content` 是一个字符串（str），不是数据结构。**模型上辈子是聊天机器人，这辈子还是——它吐出来的永远是"一段文本"。这段文本*长得像* JSON，但它不是 JSON 对象，是"写着 JSON 文字的字符串"。程序要用它，必须先过 `json.loads()` 这道关；而**这道关随时可能失败**。所以：让模型输出给程序读的东西，**永远要有兜底——模型输出不可全信**。

眼见为实。在热身代码的末尾加两行：

```python
content = data["choices"][0]["message"]["content"]
print(type(content))     # <class 'str'>   ← 不是 dict，是字符串
```

你想直接 `content["情感"]`？`TypeError` 伺候。字符串和字典之间隔着一堵墙，`json.loads` 是唯一的门——而门是会锁上的。

### §1.1 动笔：预测失败（5 分钟）

不加任何约束，你在 prompt 里写一句"请输出 JSON"，模型可能以哪些方式坏掉？**凭直觉先写 3 种**（写在哪都行，别只想想），写完再去对照：

→ **[对照答案（实测高频的 7 种）](0002-answers.md#sec-1-1)**（答案单独放一个文件，防手滑瞟到）

> ⚠️ **本课避坑**
> 最大的错觉是"开了 JSON mode 就高枕无忧"。`response_format` 是**提高守规矩的概率**，不是**保证**——DeepSeek 官方文档白纸黑字：JSON 模式下**有概率返回空的 `content`**。所以兜底不是"以防万一"的防御性编程姿态，是常规代码路径：线上跑一万条，每一种失败你都会撞上。

---

## §2 两招让模型说 JSON（20 分钟）

约束模型只有两招：**官方通道**（`response_format`）和**民间偏方**（prompt 里写 Schema）。两招都要会——第 3 课的 function calling 是官方通道的完全体，而民间偏方走到哪家模型上都吃。

### §2.1 招式一：response_format（官方通道）

在请求体里加一个参数，就这一行：

```python
payload = {
    "model": MODEL,
    "messages": messages,
    "response_format": {"type": "json_object"},   # ← 官方通道
}
```

DeepSeek 对这一招有**两条规矩**，都是官方文档明示的：

1. **prompt 里必须出现 "json" 字样**，最好再给一个格式示例——不然直接 400 拒绝你（返回体里会写原因，速查表 §5 的老朋友）。这不是 bug，是它强制你在调用前想清楚要什么格式。
2. **有概率返回空 content**：模型把力气全花在内部推理上，最后什么都没吐出来。识别很简单——`content` 是个空串。

（第三条算送分：DeepSeek 只支持 `json_object`，不支持 `json_schema`。）

### §2.2 招式二：Schema 写进 prompt（民间偏方）

不依赖任何参数，把格式要求完整写进 system prompt：

```python
SYSTEM_PROMPT = """你是商品评论分析器。只输出一个 JSON 对象，不要输出任何其他文字。
格式：
{"情感": "正面|负面|中性", "类别": "质量|物流|价格|服务|其他", "置信度": 0到1之间的小数}
示例：
输入"快递两天就到了，质量意外地好" → 输出 {"情感": "正面", "类别": "物流", "置信度": 0.9}
字段一个都不能多、不能少。"置信度"必须是数字，不要加引号。"""
```

两招摆一起看：

|                        | 招式一 response_format        | 招式二 Schema 进 prompt     |
| ---------------------- | --------------------------- | ------------------------ |
| 守规矩概率                | 高（协议层约束）                | 中（靠模型自觉）               |
| 换供应商                  | 各家行为不一，要逐家核对            | **零改动**，哪家都吃           |
| 空输出风险                | DeepSeek 官方明示存在          | 低                       |
| 字段级校验                 | **没有**——只保证"是个合法 JSON"  | **也没有**——还是要自己校验      |

注意最后一行：**两招都不校验字段**。`json_object` 只保证"整体是个合法 JSON"，不保证字段齐、类型对。所以无论哪招，本地解析 + 校验都省不掉——这正是兜底存在的原因。

### §2.3 失败模式解剖：一张抓失败的地图

§1.1 你预测过的失败，这里给每一条配上**识别特征**——练习里写代码抓的就是这些特征：

| 失败模式        | 识别特征                                  | 第一反应                    |
| ----------- | ------------------------------------- | ----------------------- |
| 代码围栏        | content 以三个反引号开头                     | 剥掉围栏再解析                 |
| 前后闲话        | 首字符不是 `{`                             | 截取第一个 `{` 到最后一个 `}`     |
| 空 content   | `content` 为空串                         | 触发重试                    |
| 半截 JSON     | `finish_reason == "length"`（第 1 课老朋友） | 调大 max_tokens 重发        |
| 非法语法        | `json.loads` 抛 `JSONDecodeError`      | 报错回传修复                  |
| 类型漂移        | 解析成功，但 `置信度` 是字符串                    | 本地校验捕获，修复或重试           |

### §2.4 兜底阶梯（本课要练成的肌肉记忆）

从便宜到贵，逐级升级；上一级失败才走下一级：

```
1. 预处理     剥围栏、截取 { 到 }         ← 免费，纯字符串操作
2. 解析       json.loads + try/except   ← 免费
3. 重试一次    同样的请求再发一遍            ← 一倍 token，很多失败只是随机抖动
4. 回传修复    坏输出 + 报错原文喂回模型     ← 更贵，治"模型不知道自己错了"
5. 放弃策略    默认值 / 上抛异常 / 记日志    ← 兜底的兜底
```

第 4 级值得多看一眼——它是本课任务 2 的主角，也是 agent 世界最重要的模式之一，**错误回传**：模型犯错时，不崩、不吞，把"你刚才输出的是这个，报错是这个，修好它"作为新一轮 messages 发回去。第 5 课的工具错误处理，内核就是这一招。

### §2.5 换供应商怎么变（智谱 / Qwen 速查）

| 供应商        | 支持类型                                      | 硬性要求 / 已知坑                                          |
| ---------- | ----------------------------------------- | ---------------------------------------------------- |
| DeepSeek   | `json_object`                             | prompt 必须含 "json" 字样；**有概率返回空 content**            |
| 智谱 GLM    | `json_object`                             | 官方未演示 `json_schema`；推荐 Schema 进 system prompt + 本地校验 |
| Qwen（百炼）   | `json_object`；`json_schema` 仅部分高端模型        | messages 必须含 "JSON" 字样否则 400；开结构化输出时**不要设 max_tokens** |

（2026-08-29 依据各家官方文档核实；细节和文档入口见[速查表 §7](../reference/chat-completions-cheatsheet.md)。）

---

## §3 练习：80 分钟，主菜上桌

全部代码放在 `01_API基础/`。地基就是热身那次调用——把它包装成函数，本课反复用：

```python
# ex3_reviews.py 顶部 —— 调用函数（地基，只给姿势）
import os
import json
import requests

def chat(messages: list) -> str:
    """发一轮对话，返回 content 字符串。"""
    resp = requests.post(
        f"{os.environ['LLM_BASE_URL']}/chat/completions",
        headers={"Authorization": f"Bearer {os.environ['LLM_API_KEY']}"},
        json={
            "model": os.environ["LLM_MODEL"],
            "messages": messages,
            "temperature": 0,        # ← 分类要稳定，随机度拧到最低
        },
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]
```

`temperature: 0` 是本课唯一的新参数。它救不了结构，但能少点火。

### 任务 1 · 评论分类器（60 分钟）

新建 `ex3_reviews.py`。目标：输入一条商品评论，程序拿到一个能用的 `dict`。

**第 1 步（15 分钟）· 招式二先行**：把 §2.2 的 system prompt 抄进去（改成你自己的措辞更好），写 `classify(review: str) -> dict`：

```python
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user",   "content": review},
]
content = chat(messages)
data = json.loads(content)    # ← 裸解析。先不要 try/except——就是要亲眼看它崩
```

**第 2 步（10 分钟）· 准备弹药**：8 条测试评论存进列表——3 条正常（正/负/中性各一），加上**压测三件套**：

```python
reviews = [
    "快递两天就到了，质量意外地好",
    "用了三次就坏了，客服还踢皮球",
    "东西还行，价格一般",
    "@@##￥%%……&**（（——乱码输入",
    "",                                # 空文本
    "很好用，" * 200,                    # 超长文本
    # ……自己再加两条你觉得刁钻的
]
```

**第 3 步（20 分钟）· 裸奔压测**：循环跑全部评论，`json.loads` 不加保护。**逐条记录**：哪条成功、哪条以什么方式崩——对号入座 §2.3 的失败模式表。这份记录就是你的"实测失败清单"，复盘题 1 的答案从这里来，**别编，要真见过**。

注意一个微妙的事：有些输入会得到"合法但离谱"的 JSON（比如乱码评论被判成 `置信度: 0.999` 的正面）——**解析成功不代表结果可用**。这笔账先记着，学有余力再算。

**第 4 步（15 分钟）· 换招式一对比**：请求体加上 `"response_format": {"type": "json_object"}`（确认 prompt 里有 "json" 字样——§2.1 规矩 1），重跑压测。对比两招的失败清单：哪些失败消失了？新失败（比如空 content）出现了吗？

### 任务 2 · 加兜底（20 分钟）

现在把崩掉的地方一层层垫起来。先写 `parse_review(content: str) -> dict`，实现兜底阶梯的 1–2 级：

1. **预处理**：剥代码围栏（把首尾的反引号和围栏标记 `strip()` 掉）、截取第一个 `{` 到最后一个 `}`。
2. **解析**：`json.loads` 包上 try/except；失败时抛自定义异常 `BadJSON`，**把原始 content 和报错信息都带上**——第 4 级兜底要用它们。

然后把 `classify` 升级成三级兜底：

3. 解析失败 → **原样重试一次**（temperature 已是 0 还失败，说明真不是抖动）。
4. 仍失败 → **回传修复**：

```python
messages = [
    {"role": "system",    "content": SYSTEM_PROMPT},
    {"role": "user",      "content": review},
    {"role": "assistant", "content": 坏的content},      # ← 模型上次的坏输出，以 assistant 身份进历史
    {"role": "user",      "content": f"你上一条输出不是合法JSON，"
                                       f"json.loads 报错：{报错信息}。"
                                       f"重新输出，只要那个JSON。"},
]
content = chat(messages)    # 拿到修复版，再走一遍 parse_review
```

看清楚这段 messages——**这就是第 1 课讲的"多轮对话"**：坏输出以 assistant 身份进历史，报错作为新的 user 消息发回。你还没写过聊天机器人，已经完成了一轮人机协作修 bug。

> ✅ **验收标准**
> 压测三件套（乱码、空文本、超长）全部有明确出路：要么解析成功，要么走完兜底阶梯后得到一个**明确的失败结果**（比如返回 `None` 并打印日志）——**不再有任何一条让程序裸崩**。

### 自查清单

- [ ] 两招都实测过，各有一份失败清单
- [ ] 空 content 亲手见过至少一次（DeepSeek 会送的，多跑几轮压测）
- [ ] `parse_review` 能剥围栏、截花括号
- [ ] 回传修复的 messages 拼对了——能指出坏输出是哪条 role、报错是哪条 role
- [ ] 全部测试评论跑完，程序零裸崩

> 💡 **卡住 20 分钟就求助**
> 老规矩：期望什么、实际发生什么、完整报错、相关代码，四样贴给我。压测撞上离谱输出也直接贴过来——真实的失败样本比任何教材都值钱。

---

## §4 复盘：10 分钟检索练习

规则不变：**合上代码**，先在心里完整说出来，再去[答案册](0002-answers.md)对照。答完把计划里两道复盘问题的口述答案发给我，我来判卷：

1. 列出你实测遇到的至少 3 种 JSON 输出失败方式，各自的兜底策略是什么？
2. 为什么说结构化输出是 agent 的地基——它和下一次要学的 tool calling 是什么关系？

自测五题（每题先默答，再点「看答案」跳到答案册）：

**Q1. `resp["choices"][0]["message"]["content"]` 拿到的是什么类型？程序消费它之前必须过哪道关？**
→ [看答案](0002-answers.md#q1)

**Q2. DeepSeek 的 `json_object` 模式有哪两条官方明示的规矩？**
→ [看答案](0002-answers.md#q2)

**Q3. 兜底阶梯里，为什么"原样重试"排在"报错回传修复"前面？**
→ [看答案](0002-answers.md#q3)

**Q4. 半截 JSON（截断）怎么在解析之前就识别出来？**
→ [看答案](0002-answers.md#q4)

**Q5. 同样是"让模型给参数"，在 prompt 里求它输出 JSON 和下一课的 tool calling，本质区别是什么？**
→ [看答案](0002-answers.md#q5)

---

## §5 下课

**学有余力（可选）**：给分类器加**字段校验**——`类别` 不在白名单里、`置信度` 不是 0–1 的数字，都算失败、走兜底。做完你会体会到：**解析成功只是及格线，校验才是可用线。**

**第 1 课的欠账**：ex2（多轮聊天机器人）还没做。好消息是任务 2 的"回传修复"本身就是一次微型多轮对话——messages 你已经亲手拼过一轮了。找个 20 分钟把 ex2 补上，会比从零做快得多。

**完成后回来找我**：报告练习完成情况（附上你的实测失败清单更好），我帮你勾掉计划里的 checkbox、写学习档案、判卷复盘口述题。然后随时可以喊"开始第 3 次课"——**Function Calling：让模型驱动你的代码**。今天你在 prompt 里"求"模型说机器话，下一课换成官方协议"命令"它交参数——同一个问题的官方答案。到时候你会发现，兜底照样一个都少不了，但腰杆直了很多。

> 💡 **我是你的导师，不是课件**
> 这页是提词器，提问的地方在对话框里。任何"为什么"、任何报错、任何"我感觉哪里不对"，直接问——卡点不过夜，是 20 小时速通的前提。

---

*上一课：[第 1 课 · LLM API 的本质](0001-llm-api-stateless-messages.md) ｜ 下一课：第 3 课 · Function Calling（完成本课后解锁）*
*AI Agent 开发 · 20 小时速通 · 总计划见 [00_20小时速通计划.md](../00_20小时速通计划.md) · [API 速查表](../reference/chat-completions-cheatsheet.md)*
