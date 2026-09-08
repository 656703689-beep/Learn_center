import json


response_text = '{"reply": "三组都通过，可以进入下一步", "passed_groups": 3, "total_groups": 3}'

response = json.loads(response_text)

print("AI回复：", response["reply"])
print("通过组数：", response["passed_groups"])
print("总组数：", response["total_groups"])