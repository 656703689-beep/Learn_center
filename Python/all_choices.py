import json

response_text = '{"choices": [{"message": {"role": "assistant", "content": "第一步检查输入"}}, {"message": {"role": "assistant", "content": "第二步检查条件"}}, {"message": {"role": "assistant", "content": "最后整理回答"}}]}'

response = json.loads(response_text)
choices = response["choices"]
for choice in choices:
    message = choice["message"]
    print("角色：", message["role"])
    print("内容：", message["content"])
# 在下面补全：逐份读取 message，再打印 content