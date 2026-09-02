# epochs = int(input("准备模拟几轮训练？"))
# for epoch in range(1,epochs + 1):
#     print(f"第{epoch}轮")
# print("全部完成")
# score = 60
# target_score = int(input("请输入目标分数："))
# for epoch in range(1,4):
#     score = score + 5
#     print(f"第{epoch}轮,分数：{score}")
#     if score >= target_score:
#         print("分数达标,停止训练")
#         break
# if  score < target_score:
#     print("训练结束,未达到目标")
# else:
#     print("训练结束,目标已完成")
# import random
# secret = random.randint(1, 30)
secret = 30
max_attempts = 8
for attempt in range(1,max_attempts + 1):
    guess = int(input(f"第{attempt}次猜数字:"))
    if guess == secret:
        print("猜中了")
        break
    elif guess < secret:
        print("没猜中，太小了，请你继续猜，小笨蛋")
    else:
        print("太大了,大笨蛋,脑子有洞")
    remaining = max_attempts - attempt
    if remaining > 0:
        print(f"还剩{remaining}次机会")
if guess != secret:
    print(f"{max_attempts}次机会已用完,大sb")
    print(f"正确答案是:{secret}")