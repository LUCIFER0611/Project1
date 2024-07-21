from sklearn.mixture import GaussianMixture

def cluster_embeddings(embeddings, n_clusters=10):
    gmm = GaussianMixture(n_components=n_clusters, covariance_type='tied')
    gmm.fit(embeddings)
    return gmm.predict_proba(embeddings)

clusters1 = cluster_embeddings(embeddings1)
clusters2 = cluster_embeddings(embeddings2)
clusters3 = cluster_embeddings(embeddings3)
import openai

openai.api_key = sk-proj-erYzibAcRw0eWXSfsuJET3BlbkFJbwlfsEwRWNVHxX0sZvAi

def summarize_cluster(cluster_texts):
    prompt = "Summarize the following texts:\n" + "\n".join(cluster_texts)
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    summary = response.choices[0].text.strip()
    return summary

# Example Usage
summaries1 = [summarize_cluster([chunks1[i] for i in range(len(chunks1)) if clusters1[i][cluster_index] > 0.5]) for cluster_index in range(10)]
from pymilvus import connections, utility, FieldSchema, CollectionSchema, DataType, Collection

connections.connect("default", host="localhost", port="19530")

# Define schema
fields = [
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
    FieldSchema(name="metadata", dtype=DataType.STRING)
]
schema = CollectionSchema(fields, "Textbook RAPTOR Index")

# Create collection
collection = Collection("raptor_index", schema)
collection.insert([embeddings1 + embeddings2 + embeddings3, metadata])

# Example metadata: [{"textbook": "textbook1", "page_number": 1, "summary": "summary_text"}]
