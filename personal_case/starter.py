from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding  # 新增导入
import asyncio
import os

# 配置嵌入模型的 api_base
embed_model = OpenAIEmbedding(
    # model="ext-embedding-ada-002",
    api_base="https://api.nuwaapi.com/v1"  # 替换为实际的 API base URL
)


# Create a RAG tool using LlamaIndex
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
query_engine = index.as_query_engine(llm=OpenAI(model="gpt-4o-mini",api_base="https://api.nuwaapi.com/v1"))

# print(query_engine.query("What did the author do in college?"))

# Define a simple calculator tool
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b


async def search_documents(query: str) -> str:
    """Useful for answering natural language questions about an personal essay written by Paul Graham."""
    response = await query_engine.aquery(query)
    return str(response)

# Create an enhanced workflow with both tools
agent = FunctionAgent(
    name="Agent",
    description="Useful for multiplying two numbers and searching through documents to answer questions.",
    tools=[multiply, search_documents],
    llm=OpenAI(model="gpt-4o-mini",
               api_base="https://api.nuwaapi.com/v1"),
    system_prompt="""You are a helpful assistant that can perform calculations
    and search through documents to answer questions.""",
)


# Now we can ask questions about the documents or do calculations
async def main():
    response = await agent.run(
        "What did the author do in college? Also, what's 7 * 8?"
    )
    print(response)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())