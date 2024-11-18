import os
import ollama

import constants.constants_retrieval as constants

from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain_ollama import OllamaEmbeddings

def retrieve_tokens(query, context):

    clean_context = context[:-1] 

    formatted_chat_history = "\n".join(f"{item['role']}: {item['content']}" for item in clean_context)

    llm = OllamaLLM(model=constants.MODEL)
    prompt = ChatPromptTemplate.from_template(constants.TEMPLATE)

    embeddings = OllamaEmbeddings(
        model="mxbai-embed-large",
    )

    # embeddings = HuggingFaceEmbeddings(model_name=model)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    chroma_data_path = os.path.join(base_dir, "../chromeDB_storage")

    vector_db = Chroma(embedding_function=embeddings, persist_directory=chroma_data_path, collection_name="rag-chroma")
    retriever = vector_db.as_retriever()

    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

    result = rag_chain.invoke({"context": formatted_chat_history, "input": query})
    return result["answer"]