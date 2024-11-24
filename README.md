# Offline Retrieval-Augmented Generation (RAG) Chatbot
This project is a Retrieval-Augmented Generation (RAG) chatbot designed to provide accurate, personalized answers by leveraging personal data stored in documents like text files or PDFs. It ingests and processes this data to generate responses specific to the user's background, such as their resume details.

## Features
* **Data Ingestion**:
  
  * Supports ingestion of text files (.txt) and PDFs (.pdf).
  * Automatically extracts relevant information for retrieval-based response generation.
  
* **Personalized Q&A**:
  
  * Answers questions based on the ingested data, simulating human-like conversational abilities.
  * Ideal for job application queries or personal background checks.
    
* **Scalable and Efficient**:
  
  * Modular design for adding additional document types or data sources.
  * Handles large documents with optimized retrieval pipelines.

## Installation
1. **Clone the repository**:

```bash
git clone https://github.com/Q-Dead/RAG-based_AI_App 
cd rag-chatbot
```

2. **Set up the environment:**
   
  Create a virtual environment and install dependencies.

```bash
python -m venv .venv
```
**Linux/MacOS**
```bash
source .venv/bin/activate
```
**Windows**
```bash
.\.venv\Scripts\activate
```
```bash
pip install -r requirements.txt
``` 
3. **Install additional tools:**
Ensure tools for PDF processing (e.g., PyMuPDF) and embeddings (e.g., sentence-transformers) are installed.

## Usage
### 1. Add Personal Data
Place the resume or text files in the data/ directory. Example files:

* data/resume.pdf
* data/background.txt
  
### 2. Run the Chatbot
Start the chatbot:

```bash
streamlit run .\src\main.py
```
### 3. Ask Questions
Example queries:

"What is the applicant's educational background?"

"List their programming skills."
