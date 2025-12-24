from langchain_ollama import ChatOllama

# 设置本地模型，不使用深度思考
model = ChatOllama(base_url="http://127.0.0.1:11434", model="qwen3-vl:8b", reasoning=False)
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]

ai_msg = model.invoke(messages)

print(ai_msg.content)
"""# 打印结果
print(model.invoke("什么是LangChain?"))"""