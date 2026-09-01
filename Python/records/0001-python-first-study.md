# Python 第 1 次学习记录

日期：2026-09-01

## 已完成

- 能独立运行 `study_log.py`。
- 写出了温度换算脚本：摄氏度转华氏度。
- 写出了 BMI 计算脚本，并修正了 BMI 公式。
- 写出了猜数字脚本，并完成 `if / elif / else` 三个分支验证。

## 已掌握

### 输入和输出

`input()` 用来接收用户输入，返回值是 `str`。

`print()` 用来把结果输出到终端。

### 类型转换

用户输入默认是文本，所以做数学计算前要转换类型：

```python
minutes = int(input("今天计划学习多少分钟？"))
celsius = float(input("请输入摄氏温度："))
```

`int()` 转整数，`float()` 转小数。

### 变量

变量用来保存数据：

```python
secret = 7
guess = int(input("猜一个1到10的数字"))
```

`=` 是赋值，把右边的值放进左边的变量。

### 数学计算

BMI 公式是：

```python
bmi = weight / (height ** 2)
```

`height ** 2` 表示身高的平方，也就是：

```python
height * height
```

不是：

```python
height * 2
```

### 条件判断

猜数字脚本使用了条件判断：

```python
if guess == secret:
    print("猜对了")
elif guess > secret:
    print("猜大了")
else:
    print("猜小了")
```

`==` 是判断是否相等。

`else` 不写条件，因为它表示“前面的条件都不满足时执行”。

### 缩进

`if / elif / else` 后面要加冒号 `:`。

属于某个分支的代码要缩进 4 个空格：

```python
if guess == secret:
    print("猜对了")
```

## 本次修正过的错误

1. 误以为 `input()` 返回的就是数字。

   正确理解：`input()` 返回 `str`，需要用 `int()` 或 `float()` 转成数字。

2. BMI 公式写成了：

   ```python
   bmi = weight / (height * 2)
   ```

   正确写法：

   ```python
   bmi = weight / (height ** 2)
   ```

3. 把 `else` 写成了带条件的形式：

   ```python
   else guess > secret:
   ```

   正确写法：

   ```python
   elif guess > secret:
   ```

## 验证结果

猜数字脚本验证通过：

```text
输入 7 -> 猜对了
输入 8 -> 猜大了
输入 6 -> 猜小了
```

## 下次学习建议

下一次进入 Python 的循环：

```python
while
```

目标：让猜数字程序可以一直猜，直到猜对为止。
