# Textbook QA System

## Project Structure

- **Content Extraction:** Code for extracting text from textbooks.
- **Data Chunking:** Code for chunking the extracted text.
- **RAPTOR Indexing:** Code for creating the RAPTOR index using MILVUS.
- **Retrieval Techniques:** Code for implementing query expansion and hybrid retrieval methods.
- **Re-ranking:** Code for re-ranking the retrieved data.
- **Question Answering:** Code for the question answering system using an LLM.
- **User Interface (Optional):** Code for the Streamlit user interface.

## Setup Instructions

### Dependencies

Install the required libraries:
```bash
pip install pymupdf
pip install nltk
pip install sentence-transformers
pip install scikit-learn
pip install pymilvus
pip install pyserini
pip install transformers
pip install openai
pip install streamlit
