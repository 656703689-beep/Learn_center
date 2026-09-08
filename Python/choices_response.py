import json


response_text = '{"choices": [{"message": {"role": "assistant", "content": "第一组通过，第二组继续测试"}}], "usage": {"total_tokens": 156}}'

response = json.loads(response_text)

choices = response["choices"]
first_choice = choices[0]
message = first_choice["message"]
usage = response["usage"]

print("角色：", message["role"])
print("内容：", message["content"])
print("token数量：", usage["total_tokens"])