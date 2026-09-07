def compare_guess(guess,secret):
    if guess < secret:
        return "太小了"
    elif guess > secret:
        return "太大了"
    else:
        return "猜中了"
guesses = [30,31,29]
secret = 30
results = []
for guess in guesses:
    result = compare_guess(guess, secret)
    results.append(result)
print(results)
