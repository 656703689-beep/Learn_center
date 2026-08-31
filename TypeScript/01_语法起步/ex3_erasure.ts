const price1 : number = 9.9;
const title : string = "TypeScript 入门";
const isPublished : boolean = true;
const tags : string[] = ["TS", "JS", "前端"];
const nums : number[] = [1, 2, 3, 4, 5];

function add(x: number, y: number): number {
    return x + y;
}

function size(n: number): "small" | "large" {
    return n < 100 ? "small" : "large";
}
console.log(size(50));

const result : number = add(1, 2);
console.log(result);

const data: { name: string } = JSON.parse('{"nama": "typo"}'); // JSON.parse返回的是any类型，TS无法检查其结构
console.log(data.name);         // ← 打印什么？先预测再跑  答：打印undefined，因为JSON字符串中没有name属性，只有nama属性，所以data.name是undefined
console.log(data.name.length);  // ← 发生什么？先预测再跑  答：发生运行时错误，因为data.name是undefined，undefined没有length属性，所以会抛出TypeError: Cannot read property 'length' of undefined

// ── 编译观察（npx tsc --strict --outDir tmp --ignoreConfig ex3_erasure.ts，对照 tmp/ex3_erasure.js）──
// 消失了：变量后面的类型注解， : number、: string、: boolean、: string[]、: number[]。
// 留下了：变量的初始化值和函数体，9.9、"TypeScript 入门"、true、["TS", "JS", "前端"]、[1, 2, 3, 4, 5]、add()。
// 补一眼：size 的返回类型 "small" | "large"（字面量联合）同样消失——产物里只剩 function size(n) { ... }，返回值照常工作，没人再管它只能是这两个词。