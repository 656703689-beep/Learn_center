import json


reports = [
    {"name": "第一组", "hits": 1},
    {"name": "第二组", "hits": 0}
]

json_text = json.dumps(reports, ensure_ascii=False)

print(json_text)