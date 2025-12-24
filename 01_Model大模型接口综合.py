from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 设置本地模型，不使用深度思考
model = ChatOllama(base_url="http://127.0.0.1:11434", model="qwen3-vl:8b", reasoning=False)

# 将多个问题合并为一个消息
messages = [
    SystemMessage(content="你叫小亮，是一个乐于助人的人工助手"),
    HumanMessage(content="请依次回答以下问题：\n1. 你是谁？\n2. 什么是LangChain？\n3. Python的生成器是做什么的？")
]

# 流式输出
response = model.stream(messages)
for chunk in response:
    print(chunk.content, end="", flush=True)
print(type(response))
