from llama_index.core.settings import Settings
from llama_index.embeddings.openai import OpenAIEmbedding

# 创建自定义的嵌入模型实例
custom_embed_model = OpenAIEmbedding(api_base = "https://api.nuwaapi.com/v1")

# 修改默认的嵌入模型
Settings.embed_model = custom_embed_model

# 打印修改后的嵌入模型
print(Settings.embed_model)
