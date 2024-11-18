import os
from retrieval import retrieve_tokens
from typing import Final
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


import doc_proc.document_processors
from embedding import text_embedding_to_chromaDB

MODEL: Final[str] = "llama3.2"

TEMPLATE = (
"""SYSTEM:
You are an AI assistant specialized in providing detailed and insightful answers about the person's resume using retrieval-augmented generation. Use the provided resume information to answer questions accurately, concisely, and professionally. If necessary, provide context or elaborate to clarify the information. Always reference the data in the resume to ensure factual consistency.

User Question:
"Can you tell me more about [specific person's name]?"

Expected AI Behavior:
1. Search and retrieve relevant details about the person's resume, such as their trainings, skills, education and work experience.
2. Summarize the information in an easy-to-understand format.
3. If specific details are not in the resume, respond with something like: "The resume does not provide specific details on that topic."

Additional Context:
The resume is formatted with sections such as "WORK EXPERIENCE," "EDUCATION," "TRAININGS," and "Skills." The AI can also highlight unique accomplishments or notable expertise if present. Scope is sometimes considered as skill.

Current Conversation
{context}
human:{input}
AI:
"""
)

prompt = ChatPromptTemplate.from_template(TEMPLATE)

FF = doc_proc.document_processors.get_pdf_documents()
TT = doc_proc.document_processors.get_txt_files()

rr = FF + TT

text_embedding_to_chromaDB(rr)

query = input("Enter Questions: ")

print(retrieve_tokens(query))