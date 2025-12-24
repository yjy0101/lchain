import os
import dotenv
from langchain_classic. agents import create_tool_calling_agent, AgentExecutor
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import Tool  # ← 用这个代替 GoogleSearchRun
from langchain_ollama import ChatOllama

# 加载环境变量配置文件
dotenv.load_dotenv()

# 从环境变量中获取 Serper API 密钥
api_key = os.getenv("SERPER_API_KEY")

if not api_key:
    raise ValueError("❌ SERPER_API_KEY 未在环境变量中设置")

# 创建 Serper API 包装实例
api_wrapper = GoogleSerperAPIWrapper()

# ✅ 使用 Tool 包装搜索功能（而不是 GoogleSearchRun）
search_tool = Tool(
    name="Google Search",
    func=api_wrapper.run,
    description="用于搜索最新的网络信息。输入应是一个搜索查询。"
)

# 将搜索工具添加到工具列表中
tools = [search_tool]

# 定义聊天提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个助人为乐的助手，并且可以调用工具进行网络搜索，获取实时信息。"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# 创建 Ollama 聊天模型实例
llm = ChatOllama(base_url="http://127.0.0.1:11434", model="qwen3:14b")

# 创建工具调用代理
agent = create_tool_calling_agent(llm, tools, prompt=prompt)

# 创建代理执行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 调用代理执行器
result = agent_executor.invoke({"input": "小米最近发布的新品是什么？"})
print(result)