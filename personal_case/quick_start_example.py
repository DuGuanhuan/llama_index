from llama_index import VectorStoreIndex, SimpleDirectoryReader

# 读取文档
documents = SimpleDirectoryReader('data').load_data()

# 创建索引
index = VectorStoreIndex.from_documents(documents)

# 创建查询引擎
query_engine = index.as_query_engine()

# 进行查询
response = query_engine.query("你的查询问题")

print(response)