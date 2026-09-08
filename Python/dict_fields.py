def compare_guess(guess, secret):
    if guess < secret:
        return "太小了"
    elif guess > secret:
        return "太大了"
    else:
        return "猜中了"


def suggest_from_counts(small_count, big_count, hit_count):
    if hit_count > 0:
        return "已经猜中过，测试通过"
    elif small_count > big_count:
        return "整体偏小，可以试大一点"
    elif big_count > small_count:
        return "整体偏大，可以试小一点"
    else:
        return "偏小和偏大一样多"


def build_report(results):
    total_count = len(results)
    small_count = results.count("太小了")
    big_count = results.count("太大了")
    hit_count = results.count("猜中了")
    summary = suggest_from_counts(small_count, big_count, hit_count)

    return {
        "total": total_count,
        "small": small_count,
        "big": big_count,
        "hits": hit_count,
        "summary": summary
    }


guesses = [35, 40, 20]
secret = 30
results = []

for guess in guesses:
    result = compare_guess(guess, secret)
    results.append(result)

report = build_report(results)

print(results)
print(report)
print("偏小次数：", report["small"])
print("偏大次数：", report["big"])
print("猜中次数：", report["hits"])
print("总结：", report["summary"])