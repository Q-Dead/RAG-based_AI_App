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
   
&nbsp; &nbsp; Create a virtual environment and install dependencies.

```bash
python -m venv .venv
```
&nbsp; &nbsp; **Linux/MacOS**
```bash
source .venv/bin/activate
```
&nbsp; &nbsp; **Windows**
```bash
.\.venv\Scripts\activate
```
```bash
pip install -r requirements.txt
``` 
3. **Install Ollama Model 3.2**
Follow these steps to install Ollama:

&nbsp; &nbsp; **Windows**

&nbsp; &nbsp; Download the installer for Ollama 3.2 from the official Ollama website and follow the instructions to install it.

&nbsp; &nbsp; **macOS**
```bash
brew install ollama@3.2
```

&nbsp; &nbsp; **Linux**

&nbsp; &nbsp;For Linux-based systems, use the following commands:

```bash
wget https://ollama.com/download/ollama_3.2_linux.tar.gz
tar -xzvf ollama_3.2_linux.tar.gz
sudo mv ollama /usr/local/bin/
```

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
