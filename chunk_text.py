import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def chunk_text(text, chunk_size=100):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0
    
    for sentence in sentences:
        sentence_length = len(sentence.split())
        if current_length + sentence_length > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(sentence)
        current_length += sentence_length
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

# Example Usage
chunks1 = chunk_text(textbook_text1)
chunks2 = chunk_text(textbook_text2)
chunks3 = chunk_text(textbook_text3)
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embeddings1 = model.encode(chunks1, show_progress_bar=True)
embeddings2 = model.encode(chunks2, show_progress_bar=True)
embeddings3 = model.encode(chunks3, show_progress_bar=True)
