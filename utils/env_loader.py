import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    return {
        "OPENAI_API_KEY": os.environ["OPENAI_API_KEY"],
        "PINECONE_API_KEY": os.environ["PINECONE_API_KEY"],
        "PINECONE_ENVIRONMENT": os.environ["PINECONE_ENVIRONMENT"],
        "PINECONE_INDEX_NAME": os.environ["PINECONE_INDEX_NAME"],
        "PINECONE_NAMESPACE": os.environ["PINECONE_NAMESPACE"],
    }