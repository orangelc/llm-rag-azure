from llm.embeddings import get_embeddings
from llm.chat_model import get_chat_model
from vectorstores.pinecone import get_vectorstore
from langchain.chains import RetrievalQA
from langchain.schema import BaseRetriever



async def get_qa_chain(config):
    
    llm = get_chat_model(config["OPENAI_API_KEY"])
    embeddings = get_embeddings(config["OPENAI_API_KEY"])
    
    vectorstore = get_vectorstore(
        config["PINECONE_API_KEY"],
        config["PINECONE_ENVIRONMENT"],
        config["PINECONE_INDEX_NAME"],
        embeddings,
        config["PINECONE_NAMESPACE"]
    )

    retriever = vectorstore.as_retriever()
    assert isinstance(retriever, BaseRetriever), "El retriever no es válido"

    return RetrievalQA.from_llm(llm=llm, retriever=retriever)


