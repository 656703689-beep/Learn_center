import json

response_text = '{"choices": [{"message": {"role": "assistant", "content": "先检查输入"}}, {"message": {"role": "assistant", "content": "再检查条件"}}, {"message": {"role": "assistant", "content": "最后整理回答"}}]}'
response = json.loads(response_text)

contents = []

# 在下面补全：逐条读取 content，并 append 到 contents
for choice in response["choices"]:
    message = choice["message"]
    content = message["content"]
    contents.append(content)

print(contents)