import os
import re
from pathlib import Path

def process_metadata(loader) -> list:
    pages = []
    chunk_no = 0
    prev_page_id = None
    
    for doc in loader:
        doc.page_content = re.sub(r'[^\x00-\x7F]+', '', doc.page_content)
        filetype = Path(doc.metadata["source"]).suffix
        doc.metadata["source"] = os.path.basename(os.path.normpath(doc.metadata["source"]))
        doc.metadata["id"], prev_page_id, chunk_no = process_id_db(doc, prev_page_id, chunk_no, filetype)

        pages.append(doc)

    return pages

def process_id_db(document, prev_page_id, chunk_no, filetype) -> str:

    if filetype == '.pdf':
        filename = document.metadata.get("source")
        page_no = document.metadata.get("page")
        prefix_page_id = f"{filename}:{page_no}"
        
    elif filetype == '.txt':
        filename = document.metadata.get("source")
        prefix_page_id = f"{filename}"

    if prefix_page_id == prev_page_id:
        chunk_no += 1
    else:
        chunk_no = 0

    chunk_id = f"{prefix_page_id}:{chunk_no}"

    return chunk_id, prefix_page_id, chunk_no