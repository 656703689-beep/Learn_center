# 第 2 课 · 结构化输出：让模型说"机器话"

> **AI Agent 开发 · 20 小时速通 · 2 / 10**
> 节奏：**30 分钟学**（§0–§2，§0 含热身）→ **80 分钟练**（§3，代码放 `01_API基础/`）→ **10 分钟复盘**（§4）。
> 主线按 **DeepSeek** 写（你选定的那家）；智谱 / Qwen 的差异收在 §2.5，换供应商时回来查。
> 代码与第 1 课的 TS 版同款：Node 内建 `fetch` 裸调 HTTP，跑法 `npx tsx`——npm 项目早就装好了，今天依然什么都不用装。
> 照例提醒：本课核心认知与语言无关——"模型输出不可全信"在 Python 里成立，在 TypeScript 里照样成立。

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

### §0.1 确认 TS 环境（1 分钟）

第 1 课已经把 TS 环境搭好了（工作区根目录的 npm 项目：`tsx`、`@types/node`、`typescript` 都在，另带了 `dotenv` 和 `openai` 备用——本课仍然不用它们）。确认一下就能开工：

```bash
node --version      # 你的机器：v22.22.2，fetch 内建
npx tsx --version   # 在 01_API基础/ 里跑也没问题：npx 会自动向上找到根目录的 node_modules
```

今天所有代码都这么跑：`npx tsx 文件名.ts`。要单步调试、想在 REPL 里单独试函数？[ts-debug-repl 速查表](../reference/ts-debug-repl.md)里有现成姿势。脚本里今天只用到三样 JS 特色：`await`（等异步结果）、模板字符串（反引号包着、`${}` 插值）、`const`。别的不用管。

### §0.2 热身：用 TS 把第 1 课重做一遍（10 分钟）

第 1 课任务 1 你已经用 Python 做完了——现在把同一个最小调用翻译成 TS。**翻译本身就是最好的热身**：你会亲眼看到，除了发请求的姿势变了，请求和响应一个字都没变。

新建 `01_API基础/ex1_minimal_call.ts`：

```typescript
// 01_API基础/ex1_minimal_call.ts —— 第 1 课任务 1 的 TS 重制版
const BASE_URL = process.env.LLM_BASE_URL!;   // 末尾的 ! 表示"我确定它已设置"
const API_KEY  = process.env.LLM_API_KEY!;
const MODEL    = process.env.LLM_MODEL!;

async function main() {
  const resp = await fetch(`${BASE_URL}/chat/completions`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: MODEL,
      messages: [{ role: "user", content: "用一句话解释什么是 JSON" }],
    }),
    signal: AbortSignal.timeout(60_000),      // ← 60 秒超时
  });

  const data = await resp.json();
  console.log(resp.status);
  console.log(JSON.stringify(data, null, 2));
}
main();
```

跑通后盯住两处，后面 70 分钟全靠它们：

1. `data.choices[0].message.content`——模型的回复正文。（你的 DeepSeek 默认开着思考模式，message 里多半还有个 `reasoning_content` 字段——那是思维链，取正文不受影响，详见[速查表 §3.1](../reference/chat-completions-cheatsheet.md)。）
2. `data.usage`——计费三件套。

哪个字段干什么忘了，回[第 1 课 §2.2 的响应解剖图](0001-llm-api-stateless-messages.md)扫一眼。

> 💡 **课前读什么**
> [DeepSeek 文档](https://api-docs.deepseek.com/)里的 **JSON Output** 指南（10 分钟）。§2 讲的每条规矩都出自这里——先读原文再听我讲，体感完全不同。

---

## §1 核心认知：模型说的永远是"话"，不是"数据"

> ◆ **本课唯一必须带走的东西**
>
> **`content` 是一个字符串（string），不是数据结构。**模型上辈子是聊天机器人，这辈子还是——它吐出来的永远是"一段文本"。这段文本*长得像* JSON，但它不是 JSON 对象，是"写着 JSON 文字的字符串"。程序要用它，必须先过 `JSON.parse()` 这道关；而**这道关随时可能失败**。所以：让模型输出给程序读的东西，**永远要有兜底——模型输出不可全信**。

眼见为实。在热身代码的 `main()` 末尾加两行：

```typescript
const content = data.choices[0].message.content;
console.log(typeof content);   // "string"   ← 不是 object，是字符串
```

你想直接 `content["情感"]`？Python 会当场抛 `TypeError`，JavaScript **更客气也更阴险**：字符串取不存在的属性不报错，静默返回 `undefined`——错误被憋到下游才爆，排查起来更费劲。字符串和对象之间隔着一堵墙，`JSON.parse` 是唯一的门——而门是会锁上的。

> ⚠️ **TS 用户的专属避坑**
> **TypeScript 的类型管不到运行时。**`resp.json()` 返回 `any`——编译器对它完全放行；你给函数标的返回类型，是写给编译器的单方面合同，`JSON.parse` 出来的东西长什么样，它不查。tsx 只做转译，连类型检查都不做（想真审查就跑 `npx tsc --noEmit ex3_reviews.ts`，`typescript` 已装好，本课可选）。所以核心认知在 TS 里一字不改：**模型输出不可全信，运行时兜底永远要自己写。**类型是第一道墙（编译期），兜底是第二道墙（运行期）——两道都要有。

### §1.1 动笔：预测失败（5 分钟）

不加任何约束，你在 prompt 里写一句"请输出 JSON"，模型可能以哪些方式坏掉？**凭直觉先写 3 种**（写在哪都行，别只想想），写完再去对照：

> [!success]- 对照答案：实测高频的 7 种（先写完再展开）
> | #   | 失败方式     | 长什么样                                          |
> | --- | ---------- | ----------------------------------------------- |
> | 1   | 代码围栏     | 外面裹了一层 Markdown 代码块（三个反引号 + json 开头）      |
> | 2   | 前后闲话     | `好的，以下是你要的 JSON：{...}`                    |
> | 3   | 根本不是 JSON | 模型用 markdown 列表或纯文本回答了你的问题              |
> | 4   | 半截 JSON    | `{"情感": "正面", "类别": "物` ——输出被截断           |
> | 5   | 非法 JSON 语法 | 单引号、尾逗号、注释——`JSON.parse` 直接抛异常         |
> | 6   | 类型漂移     | 字段都在，但 `"置信度": "0.9"`（字符串，不是数字）        |
> | 7   | 字段多/少    | 多出一个你没要的 `explanation`，或漏了 `置信度`         |
>
> 一条都不是我编的——80 分钟的练习里，你会亲手撞上其中至少三种。

---

## §2 两招让模型说 JSON（20 分钟）

约束模型只有两招：**官方通道**（`response_format`）和**民间偏方**（prompt 里写 Schema）。两招都要会——第 3 课的 function calling 是官方通道的完全体，而民间偏方走到哪家模型上都吃。

### §2.1 招式一：response_format（官方通道）

在请求体里加一个参数，就这一行：

```jsonc
"response_format": { "type": "json_object" }
```

DeepSeek 对这一招有**两条规矩**，都是官方文档明示的：

1. **prompt 里必须出现 "json" 字样**，最好再给一个格式示例——不然直接 400 拒绝你（返回体里会写原因，速查表 §5 的老朋友）。这不是 bug，是它强制你在调用前想清楚要什么格式。
2. **有概率返回空 content**：模型把力气全花在内部推理上，最后什么都没吐出来。识别很简单——`content` 是个空串。

（第三条算送分：DeepSeek 只支持 `json_object`，不支持 `json_schema`。）

> ⚠️ **本课避坑**
> 最大的错觉是"开了 JSON mode 就高枕无忧"。`response_format` 是**提高守规矩的概率**，不是**保证**——DeepSeek 官方文档白纸黑字：JSON 模式下**有概率返回空的 `content`**。所以兜底不是"以防万一"的防御性编程姿态，是常规代码路径：线上跑一万条，每一种失败你都会撞上。

### §2.2 招式二：Schema 写进 prompt（民间偏方）

不依赖任何参数，把格式要求完整写进 system prompt：

```typescript
const SYSTEM_PROMPT = `你是商品评论分析器。只输出一个 JSON 对象，不要输出任何其他文字。
格式：
{"情感": "正面|负面|中性", "类别": "质量|物流|价格|服务|其他", "置信度": 0到1之间的小数}
示例：
输入"快递两天就到了，质量意外地好" → 输出 {"情感": "正面", "类别": "物流", "置信度": 0.9}
字段一个都不能多、不能少。"置信度"必须是数字，不要加引号。`;
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
| 半截 JSON     | `finish_reason === "length"`（第 1 课老朋友） | 调大 max_tokens 重发        |
| 非法语法        | `JSON.parse` 抛 `SyntaxError`          | 报错回传修复                  |
| 类型漂移        | 解析成功，但 `置信度` 是字符串                    | 本地校验捕获，修复或重试           |

### §2.4 兜底阶梯（本课要练成的肌肉记忆）

从便宜到贵，逐级升级；上一级失败才走下一级：

```
1. 预处理     剥围栏、截取 { 到 }         ← 免费，纯字符串操作
2. 解析       JSON.parse + try/catch   ← 免费
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

```typescript
// ex3_reviews.ts 顶部 —— 调用函数（地基，只给姿势）
const BASE_URL = process.env.LLM_BASE_URL!;
const API_KEY  = process.env.LLM_API_KEY!;
const MODEL    = process.env.LLM_MODEL!;

type Role = "system" | "user" | "assistant";       // 和第 1 课 ex2 同款：
interface Message { role: Role; content: string }  // role 拼错编译期就报警——TS 送的第一份礼物

async function chat(messages: Message[]): Promise<string> {
  const resp = await fetch(`${BASE_URL}/chat/completions`, {
    method: "POST",
    headers: { Authorization: `Bearer ${API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      model: MODEL,
      messages,
      thinking: { type: "disabled" },  // ← 关思考模式：分类要快、要省，且思考模式下 temperature 静默失效（速查表 §3.1）
      temperature: 0,                  // ← 随机度拧到最低——分类要稳定
    }),
    signal: AbortSignal.timeout(60_000),
  });
  if (!resp.ok) {
    throw new Error(`HTTP ${resp.status}: ${await resp.text()}`);
  }
  const data = await resp.json();          // ← 返回 any：编译器放行，风险自担（§1 避坑）
  return data.choices[0].message.content;  // 取数路径和第 1 课一模一样，只是从 [] 换成了点号
}
```

两个新参数，各就各位：`temperature: 0` 救不了结构，但能少点火；`thinking: disabled` 是 DeepSeek 的思考开关——你的 V4 默认**开着**思考，又慢又费 token，还会让 temperature 静默失效（细节见[速查表 §3.1](../reference/chat-completions-cheatsheet.md)）。分类任务直接关掉。

### 任务 1 · 评论分类器（60 分钟）

新建 `ex3_reviews.ts`。目标：输入一条商品评论，程序拿到一个能用的对象。

**第 1 步（15 分钟）· 招式二先行**：把 §2.2 的 SYSTEM_PROMPT 抄进去（改成你自己的措辞更好），给返回值定个类型，写 `classify`：

```typescript
interface Review {
  情感: "正面" | "负面" | "中性";   // ← 把"合法值"也写进类型，合同更严
  类别: string;
  置信度: number;
}

async function classify(review: string): Promise<Review> {
  const messages: Message[] = [
    { role: "system", content: SYSTEM_PROMPT },
    { role: "user",   content: review },
  ];
  const content = await chat(messages);
  return JSON.parse(content);    // ← 裸解析。先不要 try/catch——就是要亲眼看它崩
}
```

（中文当字段名和类型成员在 TS 里完全合法——分类字段是中文业务，类型就跟着业务走。）

**第 2 步（10 分钟）· 准备弹药**：8 条测试评论存进数组——3 条正常（正/负/中性各一），加上**压测三件套**：

```typescript
const reviews = [
  "快递两天就到了，质量意外地好",
  "用了三次就坏了，客服还踢皮球",
  "东西还行，价格一般",
  "@@##￥%%……&**（（——乱码输入",
  "",                      // 空文本
  "很好用，".repeat(200),   // 超长文本
  // ……自己再加两条你觉得刁钻的
];
```

**第 3 步（20 分钟）· 裸奔压测**：在 `main()` 里用 `for...of` 循环跑全部评论（循环体里 `await classify(r)`），`JSON.parse` 不加保护。**逐条记录**：哪条成功、哪条以什么方式崩——对号入座 §2.3 的失败模式表。这份记录就是你的"实测失败清单"，复盘题 1 的答案从这里来，**别编，要真见过**。

两笔账现在记下：① 有些输入会得到"合法但离谱"的 JSON（比如乱码评论被判成 `置信度: 0.999` 的正面）——**解析成功不代表结果可用**；② 这期间 `classify` 标注的 `Promise<Review>` 一声不吭——类型合同是单方面的（§1 避坑），**运行时验证就是你今天这 80 分钟的正课**。

**第 4 步（15 分钟）· 换招式一对比**：在 `chat` 的请求体里加上 `"response_format": { "type": "json_object" }`（你的 SYSTEM_PROMPT 里已有 "JSON" 字样——§2.1 规矩 1 已满足），重跑压测。对比两招的失败清单：哪些失败消失了？新失败（比如空 content）出现了吗？

### 任务 2 · 加兜底（20 分钟）

现在把崩掉的地方一层层垫起来。先写 `parseReview(content: string): Review`，实现兜底阶梯的 1–2 级：

1. **预处理**：剥代码围栏（`trim()` 掉首尾空白和反引号围栏标记）、用 `indexOf("{")` 和 `lastIndexOf("}")` 截取花括号之间那一段。
2. **解析**：`JSON.parse` 包上 try/catch；失败时抛自定义异常 `BadJSON`，**把原始 content 和报错信息都带上**——第 4 级兜底要用它们。两块姿势先给你：

```typescript
class BadJSON extends Error {
  readonly raw: string;                       // ← 坏输出的原文，回传修复时要用
  constructor(message: string, raw: string) {
    super(message);
    this.raw = raw;
  }
}
```

```typescript
// try/catch 里的姿势——TS 的 catch 变量默认是 unknown：
// 类型系统逼你先确认"它到底是什么"，才准读它的 message（又是"不可全信，先验证"）
catch (e) {
  const msg = e instanceof Error ? e.message : String(e);
  throw new BadJSON(`解析失败：${msg}`, content);
}
```

然后把 `classify` 升级成三级兜底：

3. 解析失败 → **原样重试一次**（temperature 已是 0、思考也关了还失败，说明真不是抖动）。
4. 仍失败 → **回传修复**：

```typescript
const messages: Message[] = [
  { role: "system",    content: SYSTEM_PROMPT },
  { role: "user",      content: review },
  { role: "assistant", content: badContent },  // ← 模型上次的坏输出，以 assistant 身份进历史
  { role: "user",      content: `你上一条输出不是合法JSON，JSON.parse 报错：${errorMsg}。重新输出，只要那个JSON。` },
];
const fixed = await chat(messages);   // 拿到修复版，再走一遍 parseReview
```

看清楚这段 messages——**这就是第 1 课讲的"多轮对话"**：坏输出以 assistant 身份进历史，报错作为新的 user 消息发回。你第 1 课的 ex2 用 Python 拼过一模一样的结构——语言换了，动作没换。

> ✅ **验收标准**
> 压测三件套（乱码、空文本、超长）全部有明确出路：要么解析成功，要么走完兜底阶梯后得到一个**明确的失败结果**（比如返回 `null` 并打印日志）——**不再有任何一条让程序裸崩**。

### 自查清单

- [ ] 两招都实测过，各有一份失败清单
- [ ] 空 content 亲手见过至少一次（DeepSeek 会送的，多跑几轮压测）
- [ ] `parseReview` 能剥围栏、截花括号
- [ ] 回传修复的 messages 拼对了——能指出坏输出是哪条 role、报错是哪条 role
- [ ] 能一句话说清：为什么标了 `Review` 类型，运行时校验照样不能省
- [ ] 全部测试评论跑完，程序零裸崩

> 💡 **卡住 20 分钟就求助**
> 老规矩：期望什么、实际发生什么、完整报错、相关代码，四样贴给我。想在 REPL 里单独试 `parseReview`、或单步调试看兜底怎么走？[ts-debug-repl 速查表](../reference/ts-debug-repl.md)——把骨架拆成 `llm.ts` 库文件再 `await import`，那页 §3 有现成姿势。

---

## §4 复盘：10 分钟检索练习

规则不变：**合上代码**，先在心里完整说出来，再点开下方折叠对照。答完把计划里两道复盘问题的口述答案发给我，我来判卷：

1. 列出你实测遇到的至少 3 种 JSON 输出失败方式，各自的兜底策略是什么？
2. 为什么说结构化输出是 agent 的地基——它和下一次要学的 tool calling 是什么关系？

自测五题（每题先默答，再点开「看答案」）：

**Q1. `data.choices[0].message.content` 拿到的是什么？程序消费它之前必须过哪道关？**

> [!question]- 看答案（先默答再点开）
> **字符串（typeof 是 "string"）。必须先 `JSON.parse` 解析成对象。**
>
> 模型输出的一切都是文本——长得像 JSON 的字符串依然是字符串。而这道解析关随时可能失败，所以永远要有兜底。另注意：TS 的类型标注管不到这一步（`resp.json()` 返回 any），编译器不替你把关——运行时验证照旧要自己写。

**Q2. DeepSeek 的 `json_object` 模式有哪两条官方明示的规矩？**

> [!question]- 看答案（先默答再点开）
> **① prompt 里必须含 "json" 字样，否则 400；② 有概率返回空 content。**
>
> 第一条逼你调用前想清楚格式；第二条提醒你——官方通道提高守规矩的概率，但不做保证。

**Q3. 兜底阶梯里，为什么"原样重试"排在"报错回传修复"前面？**

> [!question]- 看答案（先默答再点开）
> **因为便宜。**
>
> 重试只花一倍 token，且很多失败只是随机抖动，重发一遍就好；回传修复要多拼两条消息、更贵，只在重试也失败时才值得上。兜底阶梯的总原则：从便宜到贵，逐级升级。

**Q4. 半截 JSON（截断）怎么在解析之前就识别出来？**

> [!question]- 看答案（先默答再点开）
> **看 `finish_reason === "length"`。**
>
> 第 1 课实验 B 的老朋友：输出被 max_tokens 拦腰截断。识别出它，你就知道该调大 max_tokens 重发，而不是去"修复"一个天生残缺的 JSON。

**Q5. 同样是"让模型给参数"，在 prompt 里求它输出 JSON 和下一课的 tool calling，本质区别是什么？**

> [!question]- 看答案（先默答再点开）
> **约束力来自协议，而不是措辞。**
>
> prompt 约束靠模型自觉，输出混在 content 文本里，要你自己解析、自己兜底；tool calling 是 API 协议层的专用通道——模型把调用参数放进结构化的 `tool_calls` 字段，天生就是数据，不裹围栏、不带闲话。但注意：**参数依然要校验**（模型仍然会给错参数、编不存在的字段），所以本课练的兜底肌肉，一点都不会浪费。

---

## §5 下课

**学有余力（可选）**：给分类器加**字段校验**——`情感` 不在三个合法值里、`置信度` 不是 0–1 的数字，都算失败、走兜底；手写完一遍想上强度的，去看看 `zod` 这类 TS 运行时校验库——但先手写，知道它在帮你做什么。做完你会体会到：**解析成功只是及格线，校验才是可用线。**

**语言迁移练习（可选）**：第 1 课的 ex2 聊天机器人你用 Python 写过了；用 TS 重写一遍试试——`readline` 读输入、push 拼 messages、`node:fs` 存历史，第 1 课课件里的骨架都是现成的。第 3 课起如果继续用 TS，这一步就当提前把手感练出来。

**完成后回来找我**：报告练习完成情况（附上你的实测失败清单更好），我帮你勾掉计划里的 checkbox、写学习档案、判卷复盘口述题。然后随时可以喊"开始第 3 次课"——**Function Calling：让模型驱动你的代码**。今天你在 prompt 里"求"模型说机器话，下一课换成官方协议"命令"它交参数——同一个问题的官方答案。到时候你会发现，兜底照样一个都少不了，但腰杆直了很多。

> 💡 **我是你的导师，不是课件**
> 这页是提词器，提问的地方在对话框里。任何"为什么"、任何报错、任何"我感觉哪里不对"，直接问——卡点不过夜，是 20 小时速通的前提。

---

*上一课：[第 1 课 · LLM API 的本质](0001-llm-api-stateless-messages.md) ｜ 下一课：第 3 课 · Function Calling（完成本课后解锁）*
*AI Agent 开发 · 20 小时速通 · 总计划见 [00_20小时速通计划.md](../00_20小时速通计划.md) · [API 速查表](../reference/chat-completions-cheatsheet.md)*
