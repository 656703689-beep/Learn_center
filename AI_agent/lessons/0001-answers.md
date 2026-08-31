# 第 1 课 · 答案与提示册

> **配套课件：[0001-llm-api-stateless-messages.md](0001-llm-api-stateless-messages.md)**
>
> 答案和提示单独成册，不是为了藏，是为了**防手滑**——先自己答，答完再点过来对照。这个文件里没有新知识，全是课件里那些"卡住再看"的东西。

---

<a id="sec-1-1"></a>

## 1.1 拼 messages 的对照答案

```jsonc
[
  { "role": "system",    "content": "你是一个简洁的中文助手" },
  { "role": "user",      "content": "我叫小钟，我最喜欢的数字是 42" },
  { "role": "assistant", "content": "记住了，小钟。你最喜欢的数字是 42。" },
  { "role": "user",      "content": "我最喜欢的数字是多少？" }
]
```

数一下粗略 token：中文约每字 0.7 token，每条消息再加几个结构开销。感受一下：就这 4 条小消息，每次请求都是它们全部重新计费——对话越长，每一轮越贵。

**易错点自查**：system 是不是放在了第一条？assistant 那条是不是模型第 1 轮的原话（而不是你自己新编的）？如果这两条你写对了，无状态的核心你就抓住了。

[← 返回课件](0001-llm-api-stateless-messages.md)

---

<a id="hint-1"></a>

## 提示 1：请求和响应怎么接起来（任务 2）

发送的是**整个 messages 数组 + 新的 user 消息**；收到响应后 `const data = await resp.json()`，把 `data.choices[0].message`（它恰好就是一个 `{ role: "assistant", content: "..." }` 对象）整个 push 回同一个数组。下一轮循环发出去的，就是这个变长了的历史。

[← 返回课件](0001-llm-api-stateless-messages.md)

---

<a id="hint-2"></a>

## 提示 2：细节清单（任务 2）

用户直接回车（空输入）就 continue 跳过；`Ctrl+C` 想优雅退出可以包一层 `try/catch`；把 API 调用抽成一个 async 函数 `chat(messages: Message[]): Promise<{ content: string; usage: Usage }>`（返回回复文本和 usage），任务 3 会感谢这个设计。另外：如果拼出来的 URL 里出现 `undefined`，说明环境变量没设——回 §0 把三个 export 跑一遍。

[← 返回课件](0001-llm-api-stateless-messages.md)

---

## 自测题答案

<a id="q1"></a>

### Q1 · 两次独立调用之间，模型靠什么"知道"上一轮聊了什么？

**你把全部历史拼进本次 messages。**

API 是 stateless 的：服务器不存任何会话。上一轮的内容之所以"还在"，只因为你这次把它拼进了 messages 一起发过去。（"服务器用会话 ID 自动关联"是最大的迷惑项——没有这回事。）

[← 返回课件](0001-llm-api-stateless-messages.md)

---

<a id="q2"></a>

### Q2 · 想让第 3 轮的模型彻底"忘记"第 2 轮，正确做法是？

**删掉那轮的 user 和 assistant 两条消息。**

历史只活在你手里的列表里：物理删除那两条消息，模型就无从得知。发一条 system 命令它"忘记"没用——内容仍在 messages 里占 token，模型依然看得见。

[← 返回课件](0001-llm-api-stateless-messages.md)

---

<a id="q3"></a>

### Q3 · 想让模型全程用固定人设和规则回答，设定应放在哪里？

**第一条 system 消息里。**

system 消息写在列表开头、一次编写全程生效、指令优先级高。塞进每轮 user 消息里有时也能起效，但浪费 token 且效力不稳——人设有专属车位。

[← 返回课件](0001-llm-api-stateless-messages.md)

---

<a id="q4"></a>

### Q4 · 多轮对话进行到第 10 轮时，单次请求的 prompt token 大致怎么变？

**随历史累积而单调增长。**

每轮都是全量重发：第 10 轮的输入 = 前 9 轮全部内容 + 新消息。所以越聊越贵、越慢，直到撞上下文窗口的墙。

[← 返回课件](0001-llm-api-stateless-messages.md)

---

<a id="q5"></a>

### Q5 · 第 2 轮请求里那条 assistant 消息，是谁写进去的？

**你的代码，拼回上一轮的回复。**

模型的回复只在你拿到响应那一刻存在你的变量里。把响应里 `resp["choices"][0]["message"]` append 回 messages 的那行代码，就是你写的"记忆"。（"API 服务器自动帮你补全"不存在——服务器什么都记不住。）

[← 返回课件](0001-llm-api-stateless-messages.md)
