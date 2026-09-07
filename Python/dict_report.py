def compare_guess(guess, secret):
    if guess < secret:
        return "太小了"
    elif guess > secret:
        return "太大了"
    else:
        return "猜中了"


def suggest_from_results(results):
    hit_count = results.count("猜中了")

    if hit_count > 0:
        return "已经猜中过，测试通过"
    else:
        return "这组测试里没有猜中"


def build_report(results):
    total_count = len(results)
    hit_count = results.count("猜中了")
    summary = suggest_from_results(results)

    return {
        "total": total_count,
        "hits": hit_count,
        "summary": summary
    }


guesses = [10, 20, 25,28]
secret = 30
results = []

for guess in guesses:
    result = compare_guess(guess, secret)
    results.append(result)

report = build_report(results)

print(results)
print(report)
print("总次数：", report["total"])
print("猜中次数：", report["hits"])
print("总结：", report["summary"])