from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
import asyncio
import os

# 配置嵌入模型的 api_base
embed_model = OpenAIEmbedding(
    # model="ext-embedding-ada-002",
    api_base="https://api.nuwaapi.com/v1"  # 替换为实际的 API base URL
)

# 配置 LLM 的 api_base
llm = OpenAI(
    api_base="https://api.nuwaapi.com/v1",
    model="gpt-4o-mini"
)

try:
    # 读取文档
    documents = SimpleDirectoryReader("data").load_data()
    print(f"成功加载 {len(documents)} 个文档。")

    # 生成索引
    index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
    print("索引生成成功。") 
    print(index)

    # 生成查询引擎
    query_engine = index.as_query_engine(llm=llm)
    print("查询引擎构建成功。")
    print(query_engine)

    # 定义查询问题
    query = "请提供一些文档中的关键信息"
    # 执行查询
    response = query_engine.query(query)
    # 输出查询结果
    print(f"查询问题: {query}")
    print(f"查询结果: {response}")

except Exception as e:
    print(f"生成索引或查询引擎时出现错误: {e}")
