import os
import re

from doc_proc.data_processor import process_metadata

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader

base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir,'..', "../data")

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=150,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=True,
)

def get_pdf_documents():
    
    loader_pdf = DirectoryLoader(filepath, glob="*.pdf",  loader_cls=PyPDFLoader)
    pdf_lazy = loader_pdf.lazy_load()

    return process_metadata(text_splitter.split_documents(pdf_lazy))

def get_txt_files():

    loader_textfiles = DirectoryLoader(filepath, glob="*.txt", loader_cls=TextLoader)
    txtfile_lazy = loader_textfiles.lazy_load()

    return process_metadata(text_splitter.split_documents(txtfile_lazy))

def process_text_blocks(text_blocks, char_count_threshold=500):
    None

def save_uploaded_file(uploaded_file):
    None