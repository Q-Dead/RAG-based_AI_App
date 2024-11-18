import os
import ollama
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaEmbeddings


def text_embedding_to_chromaDB(texts) -> Chroma:

    embeddings = OllamaEmbeddings(
        model="mxbai-embed-large",
    )

    # embeddings = HuggingFaceEmbeddings(model_name=model)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    chroma_data_path = os.path.join(base_dir, "../chromeDB_storage")

    vector_db = Chroma(embedding_function=embeddings, persist_directory=chroma_data_path, collection_name="rag-chroma")

    existing_items = vector_db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])

    new_texts = []
    for text in texts:

        if text.metadata["id"] not in existing_ids:
            new_texts.append(text)

    if len(new_texts):
        new_text_ids = [text.metadata["id"] for text in new_texts]
        vector_db.add_documents(new_texts, ids=new_text_ids)

    return vector_db
