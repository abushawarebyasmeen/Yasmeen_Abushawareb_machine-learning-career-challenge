import numpy as np
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
from ..models import FAQ


tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def generate_embedding(text):
    """Generate embeddings for a given text."""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings[0]


def compute_similarity(query_embedding, stored_embeddings):
    """Compute cosine similarity between the query and stored embeddings."""
    query_embedding = np.array(query_embedding).reshape(1, -1)
    stored_embeddings = np.array(stored_embeddings)
    similarities = cosine_similarity(query_embedding, stored_embeddings)
    return similarities[0]


# Güncellenmiş: Soru ve cevabı birleştirerek embedding oluşturuyoruz
def initialize_faq_embeddings():
    faqs = FAQ.objects.filter(embedding__isnull=True)
    for faq in faqs:
        combined_text = faq.question + " " + faq.answer  # Soru + Cevap metni
        faq.embedding = generate_embedding(combined_text).tolist()
        faq.save()