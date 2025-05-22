import pinecone
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

def get_vectorstore(api_key: str, environment: str, index_name: str, embeddings):
    pinecone = Pinecone(api_key=api_key, environment=environment)
    index = pinecone.Index(index_name)
    return PineconeVectorStore(index=index, embedding=embeddings, text_key="text")