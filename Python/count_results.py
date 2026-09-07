def compare_guess(guess,secret):
    if guess < secret:
        return "太小了"
    elif guess > secret:
        return "太大了"
    else:
        return "猜中了"
guesses = [30,31,29,30]
secret = 30
results = []
for guess in guesses:
    result = compare_guess(guess, secret)
    results.append(result)
print(results)
print("太小了次数:",results.count("太小了"))
print("太大了次数:",results.count("太大了"))
print("猜中了次数:",results.count("猜中了"))