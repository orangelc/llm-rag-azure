from utils.env_loader import load_env
from chains.qa_chain import get_qa_chain

if __name__ == "__main__":
    config = load_env()
    qa_chain = get_qa_chain(config)
    query = "¿Qué puesto tiene Elena Torres?"
    response = qa_chain.invoke(query)
    print(response)