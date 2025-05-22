from langchain_openai import ChatOpenAI

def get_chat_model(api_key: str):
    return ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo", temperature=0.1)