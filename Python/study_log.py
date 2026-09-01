# """Python 第一次学习：观察一个最小程序的数据流。"""

# print("=== Python 第 1 次学习 ===")

# learner = input("你希望我怎么称呼你？ ")
# goal = "AI"
# minutes_text = input("今天计划学习多少分钟？ ")
# minutes = int(minutes_text)

# print()
# print(f"{learner}，你正在为 {goal} 学习 Python。")
# print(f"今天计划：{minutes} 分钟。")
# print(f"输入时的类型：{type(minutes_text).__name__}")
# print(f"转换后的类型：{type(minutes).__name__}")
# print("数据流：input → 变量 → 类型转换 → print")
# celsius = float(input("请输入摄氏温度:"))
# fahrenheit = celsius* 9/5+32
# print(f"{celsius}℃ = {fahrenheit:.1f}°F")
# print("温度换算完成")
# weight = float(input("体重(kg):"))
# height = float(input("身高(m)："))
# bmi = weight/(height**2)
# print(f"你的 BMI 是 {bmi:.2f}")
# secret  =   7
# guess   =   int(input("猜一个1到10的数字"))
# if  guess   ==  secret:
#     print("猜对了")
# elif guess > secret:
#     print("猜大了")
# else:
#     print("猜小了")
secret = 7
guess = 0
attempts = 0
while guess != secret:
    guess = int(input("猜一个1~10的整数:"))
    attempts = attempts+1
    if guess < secret:
        print("小了")
    elif guess > secret:
        print("大了")
print(f"猜对了!你一共猜了{attempts}次。")