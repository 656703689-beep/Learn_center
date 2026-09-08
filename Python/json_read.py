import json


json_text = '{"name": "第一组", "hits": 1, "summary": "已经猜中过，测试通过"}'

report = json.loads(json_text)

print(report)
print("组名：", report["name"])
print("猜中次数：", report["hits"])
print("总结：", report["summary"])
import json


json_text = '[{"name": "第一组", "hits": 1}, {"name": "第二组", "hits": 0}]'

reports = json.loads(json_text)

for report in reports:
    print(report["name"])
    print(report["hits"])