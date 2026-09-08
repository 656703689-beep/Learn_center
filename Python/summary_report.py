# def compare_guess(guess, secret):
#     if guess < secret:
#         return "太小了"
#     elif guess > secret:
#         return "太大了"
#     else:
#         return "猜中了"


# def suggest_from_counts(small_count, big_count, hit_count):
#     if hit_count > 0:
#         return "已经猜中过，测试通过"
#     elif small_count > big_count:
#         return "整体偏小，可以试大一点"
#     elif big_count > small_count:
#         return "整体偏大，可以试小一点"
#     else:
#         return "偏小和偏大一样多"


# def build_report(name, guesses, secret):
#     results = []

#     for guess in guesses:
#         result = compare_guess(guess, secret)
#         results.append(result)

#     small_count = results.count("太小了")
#     big_count = results.count("太大了")
#     hit_count = results.count("猜中了")
#     summary = suggest_from_counts(small_count, big_count, hit_count)

#     return {
#         "name": name,
#         "total": len(results),
#         "small": small_count,
#         "big": big_count,
#         "hits": hit_count,
#         "summary": summary
#     }


# def build_summary(reports):
#     passed_count = 0

#     for report in reports:
#         if report["hits"] > 0:
#             passed_count = passed_count + 1

#     return {
#         "total_groups": len(reports),
#         "passed_groups": passed_count
#     }


# secret = 30

# report1 = build_report("第一组", [10, 30, 40], secret)
# report2 = build_report("第二组", [35, 30, 20], secret)
# report3 = build_report("第三组", [10, 30, 25, 28], secret)

# reports = [report1, report2, report3]
# summary = build_summary(reports)

# print(summary)
# print("总组数：", summary["total_groups"])
# print("通过组数：", summary["passed_groups"])
import json

report = {
    "name": "第一组",
    "summary": "已经猜中过，测试通过"
}

json_text = json.dumps(report, ensure_ascii=False)

print(json_text)