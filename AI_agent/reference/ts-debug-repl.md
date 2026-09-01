# 速查表 · TypeScript 调试与 REPL（Node + tsx）

> **AI Agent 开发 · Reference**
> 对应 Python 的 pdb / PyCharm 调试器与 `python -i` / IPython。所有结论 2026-08-30 在 Node 22.22.2 + tsx 上实测。
> 第 1 课（TypeScript 版）配套；API 调用本身见 [chat-completions-cheatsheet.md](chat-completions-cheatsheet.md)。

---

## §1 环境前提

npm 项目在工作区根目录（`package.json` + `tsx` + `@types/node`；在 `01_API基础/` 里跑也没问题，npx 会自动向上找到它）。跑法：

```bash
npx tsx ex1_minimal_call.ts      # 跑脚本
npx tsx                          # 开 REPL（见 §3）
npx tsx -e "一行代码"             # 单行执行
```

> ⚠️ 目录名 `01_API基础` 含大写和中文，`npm init -y` 会报 Invalid name——package.json 已手写好，以后别的练习目录建 npm 项目时同样注意。

---

## §2 调试（Debug）

### 逐级武器

| 场景 | 工具 |
|---|---|
| 快速看值 | `console.log(...)` |
| 断点暂停 | `debugger;` 语句（等价 Python 的 `breakpoint()` / `pdb.set_trace()`） |
| 完整调试器 | VS Code 的 Node 调试器（见下） |
| 文件变更自动重跑 | `npx tsx watch 文件.ts` |

### VS Code 方式 A：JavaScript Debug Terminal（最像 Python，首选）

1. `Cmd+Shift+P` → 输入 `Debug: JavaScript Debug Terminal` 回车。
2. 在弹出的终端里照常 `npx tsx ex1.ts`。
3. 编辑器里点行号左侧打红点，跑到即停。

单步（F10）、步入（F11）、Watch、条件断点与 Python 的 VS Code 调试完全一致；async 代码直接断点，无需特殊处理。`debugger;` 语句在此终端下也会暂停。

### VS Code 方式 B：F5 启动（launch.json）

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "tsx 调试当前文件",
      "program": "${file}",
      "runtimeArgs": ["--import", "tsx"],
      "console": "integratedTerminal"
    }
  ]
}
```

### 不用 VS Code

```bash
npx tsx --inspect-brk ex1.ts   # 实测 tsx 转发该参数，监听 9229 端口
```

然后浏览器打开 `chrome://inspect` 连上即可；或 VS Code 里用 Attach 模式连 `127.0.0.1:9229`。

---

## §3 控制台执行函数（REPL）

**`npx tsx`（不带文件名）** = Python 的 `python -i` / IPython。实测能力：

```
$ npx tsx
> const n: number = 41      // TS 类型语法直接写
> n + 1
42                          // 变量跨行保留
> await Promise.resolve(42) // 顶层 await 直接可用
42
```

环境变量从 shell 继承：REPL 里 `process.env.LLM_API_KEY` 照常可用。

### 复用自己写的函数（本课代码组织建议）

可复用逻辑放**独立库文件**，不放会执行 main 的脚本。建 `llm.ts`：

```typescript
// 01_API基础/llm.ts —— 纯库文件：只有函数，没有顶层副作用
export async function chat(messages: Message[]): Promise<{ content: string; usage: Usage }> {
  // ……fetch 调用逻辑……
}
```

然后在 REPL 里（**必须在 `01_API基础/` 目录下启动**，相对路径才指得到）：

```
> const { chat } = await import('./llm.ts')
> await chat([{ role: "user", content: "你好" }])
```

### 两个实测出来的坑

**坑 1：`await import('./ex1.ts')` 会把文件底部的 `main()` 也执行一遍。**
Python 靠 `if __name__ == "__main__":` 挡，TS 的等价写法：

```typescript
import { realpathSync } from "node:fs";
if (process.argv[1] && realpathSync(process.argv[1]) === realpathSync(import.meta.filename)) {
  main();
}
```

必须用 `realpathSync`：macOS 有 `/private` 符号链接，`import.meta.filename === process.argv[1]` 直接比较会失败（已实测）。

**坑 2：REPL 里 import 的相对路径以启动目录为准**，不在 `01_API基础/` 里启动就找不到 `./llm.ts`。

---

## §4 Python → TypeScript 对照

| Python | TypeScript / Node |
|---|---|
| `print()` | `console.log()` |
| `breakpoint()` / `pdb.set_trace()` | `debugger;` |
| pdb / VS Code Python 调试器 | VS Code JavaScript Debug Terminal / launch.json |
| `python -i script.py` | `npx tsx` REPL + `await import(...)` |
| `python script.py` | `npx tsx script.ts` |
| 自动重载（`-X dev` / nodemon） | `npx tsx watch script.ts` |
| `if __name__ == "__main__":` | realpath 比较 guard（§3 坑 1） |
| Jupyter `.ipynb` | VS Code + Deno kernel 的 TS notebook（需装 Deno，本课不用） |
| `ipython -c "..."` | `npx tsx -e "..."` |

---

*发现与本表不符？以实测为准，然后告诉我改这里。*
