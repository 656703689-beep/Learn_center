import json


response_text = '{"message": {"role": "assistant", "content": "第二组还没有通过"}, "usage": {"total_tokens": 96}}'
response = json.loads(response_text)

message = response["message"]
usage = response["usage"]

print("角色：", message["role"])
print("内容：", message["content"])
print("token数量：", usage["total_tokens"])