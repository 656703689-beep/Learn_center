// 任务 1 · 报错观察笔记 —— 8 条故意写错的赋值（要求 5 条，超额完成）
// 观察：8 条全是同一个错误码 TS2322；报错句式固定 =「实际类型 is not assignable to 期望类型」——
// 前半段是你给的东西，后半段是注解承诺的东西。第 7 条是 strictNullChecks 在干活，
// 第 8 条是数组元素"连坐"（一个 string 混进 number[]，整行报错）。
// 错误行观察完已注释，只留原文和翻译——让项目级 npx tsc --noEmit 回到沉默（0 error）。

// 1. error TS2322: Type 'string' is not assignable to type 'number'.
// const price: number = "9.9"; // 9.9 是 number 类型，"9.9" 是 string 类型，类型不匹配

// 2. error TS2322: Type 'number' is not assignable to type 'string'.
// const str: string = 9.9;     // 9.9 是 number 类型，str 是 string 类型，类型不匹配

// 3. error TS2322: Type 'number' is not assignable to type 'boolean'.
// const isDone: boolean = 1;   // 1 是 number 类型，isDone 是 boolean 类型，类型不匹配

// 4. error TS2322: Type 'boolean' is not assignable to type 'number'.
// const num: number = true; // true 是 boolean 类型，num 是 number 类型，类型不匹配

// 5. error TS2322: Type 'boolean' is not assignable to type 'string'.
// const str2: string = false; // false 是 boolean 类型，str2 是 string 类型，类型不匹配

// 6. error TS2322: Type 'string' is not assignable to type 'boolean'.
// const isDone2: boolean = "true"; // "true" 是 string 类型，isDone2 是 boolean 类型，类型不匹配

// 7. error TS2322: Type 'undefined' is not assignable to type 'string'.
// const str3:string = undefined; // undefined 是 undefined 类型，str3 是 string 类型，类型不匹配

// 8. error TS2322: Type 'string' is not assignable to type 'number'.
// const num2:number[] = [1, 2, 3, '4']; // '4' 是 string 类型，num2 是 number[] 类型，类型不匹配
