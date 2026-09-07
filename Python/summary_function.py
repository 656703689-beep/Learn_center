def compare_guess(guess,secret):
    if guess < secret:
        return"太小了"
    elif guess > secret:
        return"太大了"
    else:
        return"猜中了"
def suggest_from_results (results):
    small_count = results.count("太小了")
    big_count = results.count("太大了")
    hit_count = results.count("猜中了")
    if hit_count > 0:
        return"已经猜中过,测试通过"
    elif small_count > big_count:
        return"整体偏小,可以试大一点"
    elif big_count > small_count:
        return"整体偏大,可以试小一点"
    else:
        return"还没有猜中,但偏小和偏大一样多"  
guesses = [10,30,40]
secret = 30
results = []
for guess in guesses:
    result = compare_guess(guess,secret)
    results.append(result)
summary = suggest_from_results(results)
print(results)
print(summary)