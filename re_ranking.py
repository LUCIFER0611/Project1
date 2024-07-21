from transformers import BertForSequenceClassification, BertTokenizer
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

def re_rank(query, documents):
    inputs = tokenizer([query] * len(documents), documents, return_tensors='pt', padding=True, truncation=True)
    outputs = model(**inputs)
    scores = torch.nn.functional.softmax(outputs.logits, dim=-1)[:, 1]  # Get scores for the "relevant" class
    return scores

# Example Usage
documents = [hit.raw for hit in hits]
scores = re_rank(query, documents)
ranked_docs = sorted(zip(scores, documents), reverse=True)
