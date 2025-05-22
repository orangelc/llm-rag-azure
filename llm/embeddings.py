from langchain_openai import OpenAIEmbeddings

def get_embeddings(api_key: str):
    return OpenAIEmbeddings(api_key=api_key, model="text-embedding-3-small")