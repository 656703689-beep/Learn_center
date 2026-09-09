import json

response_text = '{"choices": [{"message": {"role": "assistant", "content": "先检查输入"}}, {"message": {"role": "assistant", "content": "再检查条件"}}, {"message": {"role": "assistant", "content": "最后整理回答"}}]}'
response = json.loads(response_text)

contents = []

for choice in response["choices"]:
    message = choice["message"]
    content = message["content"]
    contents.append(content)

reply_count = len(contents)
final_text = "\n".join(contents)

# 在下面补全：把 contents、reply_count、final_text 放进 summary
summary = {
    "contents": contents,
    "reply_count": reply_count,
    "final_text": final_text
}
print(summary["reply_count"])
print(summary["final_text"])
print(summary["contents"])