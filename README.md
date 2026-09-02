# Learn Center

这是一个持续更新的个人学习中心，用来沉淀 Python、TypeScript 与 AI Agent 的课程、练习、速查资料和学习证据。内容以中文讲解为主，代码与技术术语保留英文。

## 学习入口

| 路线 | 当前进度 | 从这里开始 |
| --- | --- | --- |
| Python for AI | 第三课：`for` 与 `range()` 进行中 | [学习使命](Python/MISSION.md) · [第三课](Python/lessons/0003-count-with-for.html) · [学习记录](Python/NOTES.md) |
| TypeScript | 第二课：用类型建模数据 | [学习路线](TypeScript/00_学习路线图.md) · [20 小时计划](TypeScript/00_20小时速通计划.md) · [导师备忘](TypeScript/NOTES.md) |
| AI Agent | API 基础与结构化输出阶段 | [学习使命](AI_agent/MISSION.md) · [学习路线](AI_agent/00_学习路线图.md) · [20 小时计划](AI_agent/00_20小时速通计划.md) |
| Prompt 方法 | 常用提示词与学习方法 | [常用 Prompt](Prompt常用合集/常用prompt列表.md) · [快速学习框架](Prompt常用合集/快速学习框架.md) |

## 仓库结构

```text
Learn_center/
├── Python/          # Python for AI 课程、网页课件、速查与学习证据
├── TypeScript/      # TypeScript 路线、课文与练习代码
├── AI_agent/        # AI Agent 路线、课文、参考资料与阶段练习
├── Prompt常用合集/  # 可复用 Prompt 与学习方法
└── docs/agents/     # AI 工程技能使用的仓库约定
```

每条学习路线通常包含以下几类文件：

- `MISSION.md`：学习目标、完成标准与范围。
- `NOTES.md`：当前进度、环境和需要延续的教学上下文。
- `lessons/`：按编号组织的课文。
- `reference/`：随用随查的速查资料。
- `records/`：已经通过实践证明的学习成果（当前用于 Python 路线）。

## 使用方式

1. 从上表选择一条路线，先读该路线的使命或学习计划。
2. 按课文完成练习；不要只阅读，要保留运行结果、解释或复盘答案。
3. 完成一课后更新对应的 `NOTES.md`，必要时在 `records/` 留下学习证据。
4. 遇到问题时，把期望结果、实际结果、完整报错和最小相关代码一起记录。

Python 课件是静态 HTML，可以直接用浏览器打开；若浏览器限制本地资源，可在 `Python` 目录启动一个本地服务器：

```powershell
cd Python
python -m http.server 8000
```

然后访问 `http://127.0.0.1:8000/lessons/`。

## 校验

当前仓库已有的自动化校验是 Python 学习记录脚本测试：

```powershell
python -m unittest discover -s Python/tests -v
```

提交前还应检查：课程内相对链接可访问、网页控制台无错误、练习文件不包含 API key 或本地环境文件。

## 仓库协作

问题与后续任务记录在 GitHub Issues。代理工作流、标签词汇和领域文档约定见 [docs/agents](docs/agents/)。
