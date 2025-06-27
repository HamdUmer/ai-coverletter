import chromadb
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

# Load model and DB
model = SentenceTransformer('all-MiniLM-L6-v2')
client =PersistentClient(path="./chroma_db")
collection = client.get_collection("jobresume")

# Input query
query = "I need a frontend developer with django and node.js experience"

# Embed query and search
query_embedding = model.encode([query]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=2
)

print("🔍 Top matches from stored resumes:\n")
for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
    print(f"Filename: {meta['filename']}")
    print(f"Excerpt:\n{doc[:300]}...\n")
