# 教学备忘（AI 导师专用）

## 用户偏好

- 教学语言：中文；技术术语保留英文（function calling、RAG、MCP、chunk 等）
- 文档格式：markdown，与现有 `00_学习路线图.md` 风格一致（直接、重避坑、每次课有一条"核心认知"）
- **课件一律 markdown**（2026-08-28 用户明确要求：把已生成的 HTML 课件改成 markdown；此后不再产出 HTML/JS 课件）
- **不要用 `<details>` 做折叠**（2026-08-30）：用户的 markdown 查看器把 `<details>` 渲染成永远展开、点击无效。"卡住再看"的内容（提示、对照答案、自测答案）一律放独立的 `000N-answers.md`，课件里用链接跳转（锚点用显式 `<a id="...">`，纯 ASCII id）。第 1、2 课均已迁移到此模式
- 学习风格：重实操——每次 80 分钟写代码，学前阅读只给最小必读
- 复盘方式：合上代码凭记忆口述复盘问题，再验证（检索练习，非重读）

## 工作区结构

- `00_学习路线图.md`：4–6 个月长期完整路线（等级 1–5）
- `00_20小时速通计划.md`：10 次 × 2 小时速通计划（本次交付），与长期路线共存
- `01_API基础/` `02_ToolUse/` `03_RAG/` `04_多步Agent/` `05_毕业项目/`：练习代码目录（速通计划复用同一套目录）
- `RESOURCES.md`：精选资源；`MISSION.md`：学习使命

## 待确认

- MISSION.md 为推断版，等用户修正
- 用户可用的 MCP 客户端未确认（第 9 次课需要，届时确认装的是 Claude Desktop 还是其他）

## 用户环境（2026-08-28 检查）

- anaconda Python 3.13.9（/Users/clock1/tools/anaconda3/bin/python3）
- requests 2.32.5 已装；openai SDK 未装（第 1 课刻意只用 requests 裸调，第 3 课 function calling 前再决定是否引入 SDK）
- API 供应商已确认（2026-08-30）：**DeepSeek**，练手模型 `deepseek-v4-flash`；第 1 课课件的三家通用写法保留，第 2 课起课件以 DeepSeek 为主线

## 教学进度

- 2026-08-27：创建 20 小时速通计划，尚未开始第 1 次课
- 2026-08-28：第 1 次课开课。交付（markdown 版）：课件 `lessons/0001-llm-api-stateless-messages.md`（含动笔拼 messages 练习 + 5 题折叠自测）、`reference/chat-completions-cheatsheet.md`（三家供应商接入信息已核实）。早先的 HTML 版课件与 `assets/`（course.css、quiz.js）已按用户要求删除。待用户完成 80 分钟练习并回报后：勾计划 checkbox、写第一条 learning-record、判卷口述复盘题
- 2026-08-29：曾交付一版第 2 课（结构化输出），次日用户要求整体回退，已全部还原（详见 `.workbuddy-ai/memory/2026-08-30.md`）
- 2026-08-30：第 2 次课开课（重做版）。回退原因已向用户确认：当时还没准备上第 2 课（节奏问题，非课件问题）；废纸篓已清空、旧版不可找回，本次全新重写。交付：课件 `lessons/0002-structured-output.md`（以 DeepSeek 为主线；因第 1 课练习未做，§0 内置热身——速通版 ex1 最小调用）、`reference/chat-completions-cheatsheet.md` 加回 §7 结构化输出（三家核实结论沿用 08-29 版）。已知状态：第 1 课 ex1/ex2 练习未做（计划 checkbox 均未勾），第 2 课课件已提示课后补 ex2。待用户完成第 2 课 80 分钟练习并回报后：勾两课 checkbox、写 learning-record、判卷口述复盘题
- 2026-08-30：用户反馈 `<details>` 折叠在其实际查看器（浏览器内 md 预览）里无效——渲染为永远展开。已把第 1、2 课的全部折叠块迁移为独立答案册模式：新增 `lessons/0001-answers.md`、`lessons/0002-answers.md`，课件内改为锚点链接（#sec-1-1 / #hint-N / #qN）。后续课件直接沿用此模式
