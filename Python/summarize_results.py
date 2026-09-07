def compare_guess(guess,secret):
    if guess < secret:
        return"太小了"
    elif guess > secret:
        return"太大了"
    else:
        return"猜中了"
guesses = [35,40,20]
secret = 30
results = []
for guess in guesses:
    result = compare_guess(guess, secret)
    results.append(result)
small_count = results.count("太小了")
big_count = results.count("太大了")
hit_count = results.count("猜中了")
print(results)
print("太小了次数：",small_count)
print("太大了次数：", big_count)
print("猜中了次数:",hit_count)
if hit_count > 0:
    print("已经猜中过，测试通过")
elif small_count > big_count:
    print("整体偏小，可以试大一点")
elif big_count > small_count:
    print("整体偏大，可以试小一点")
else:
    print("还没猜中，但偏小和偏大一样多")
    