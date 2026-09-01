// 01_语法起步/ex4_contacts.ts —— 起步骨架（第 2 课 · 内存通讯录）
// 用法：在 TypeScript/ 根目录跑 —— npx tsx 01_语法起步/ex4_contacts.ts
// 今天两个任务都在这一个文件里：任务 1 做 TODO 0–5，任务 2 做底部的实验区

// TODO 0) 先画图纸：interface Contact ——
//        id: number（自增编号）；name: string；phone?: string（可选，有人没电话）；tags: string[]
//        再建仓库：const contacts: Contact[] = []   （数据只活在内存里，所以叫"内存通讯录"）
// TODO 1) add(...)：新建联系人 —— 分配新 id、存进仓库、把新建的联系人返回去
// TODO 2) remove(id)：删除 —— "要删的东西不存在"时返回什么，返回类型就写什么，你来定
// TODO 3) update(id, changes)：只改 changes 里给的字段，其余字段保持原样
// TODO 4) findByTag(tag)：找出带这个标签的所有联系人（一个 filter 就够）
// TODO 5) 演示区：add 三条（其中一条没有电话、一条带两个标签）→ findByTag → update →
//        删一个存在的 id 和一个不存在的 id —— 每步结果都 console.log 出来对照预期
// 完成判据：npx tsc --noEmit 沉默（四个函数的参数、返回值全有类型）+ 演示输出与预期一致

// ======================= 实验区（任务 2 · 改造实验）=======================
// TODO 6) readonly 实验：给 phone 加 readonly → 在实验区写"改属性"和"换新对象"各一行 →
//        跑 npx tsc --noEmit，把报错原文 + 一句中文翻译写在下面（格式参考课文任务 2）→
//        观察完：错误行注释掉、readonly 撤销，恢复沉默
// TODO 7) as const 实验：定义 VALID_TAGS 常量数组（as const）→ 照课文抄 type Tag = ... →
//        把 tags 相关的类型换成 Tag → 试着 add 一个非法标签 → 抄报错 → 注释掉非法行。
//        这个改造**保留**——它是通讯录的升级，不是实验废料
