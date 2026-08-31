// 01_语法起步/ex2_bmi.ts —— 起步骨架
// 用法：npx tsx ex2_bmi.ts 1.75 68

const args = process.argv.slice(2);   // ← argv 原本是 [node路径, 脚本路径, "1.75", "68"]，所以切掉前两个

const height = Number(args[0]);       // ← string → number；转不动得 NaN，不处理就是地雷
const weight = Number(args[1]);

// TODO 1) 校验：缺参（args.length）、NaN、<= 0 ——错误要 console.error 一句人话，再退出
// TODO 2) bmi(height, weight)：身高(米)、体重(kg) → number
// TODO 3) grade(bmi)：→ "偏瘦" | "正常" | "偏胖" | "肥胖"
// TODO 4) 打印 BMI 值 + 分级