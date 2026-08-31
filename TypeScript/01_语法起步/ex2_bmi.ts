// 01_语法起步/ex2_bmi.ts —— 起步骨架
// 用法：npx tsx ex2_bmi.ts 1.75 68

const args = process.argv.slice(2);   // ← argv 原本是 [node路径, 脚本路径, "1.75", "68"]，所以切掉前两个

const height = Number(args[0]);       // ← string → number；转不动得 NaN，不处理就是地雷
const weight = Number(args[1]);

if(args.length !== 2 || Number.isNaN(height) || Number.isNaN(weight) || height <= 0 || weight <= 0) {
    console.error("参数错误：请提供有效的身高（米）和体重（kg）！");
    process.exit(1); // 退出程序，状态码 1 表示错误
}
// TODO 2) bmi(height, weight)：身高(米)、体重(kg) → number
function bmi (height: number, weight: number): number {
    return weight / (height * height);
};
// TODO 3) grade(bmi)：→ "偏瘦" | "正常" | "偏胖" | "肥胖"
function grade (bmi: number): "偏瘦" | "正常" | "偏胖" | "肥胖" {
    if (bmi < 18.5) {
        return "偏瘦";
    } else if (bmi < 24) {
        return "正常";
    } else if (bmi < 28) {
        return "偏胖";
    } else {
        return "肥胖";
    }
}
// TODO 4) 打印 BMI 值 + 分级
console.log(`BMI 值: ${bmi(height, weight).toFixed(2)}`);
console.log(`分级: ${grade(bmi(height, weight))}`);
