import os 
import chromadb
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from docx import Document

# embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


client = PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection("jobresume")


def extract_text_from_doc(filepath):
    doc=Document(filepath)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])


documents=[]
metadatas=[]
ids=[]


resume_dir ="data/resume"

for i,file in enumerate(os.listdir(resume_dir)):
    if file.endswith(".docx"):
        file_path=os.path.join(resume_dir,file)
        text=extract_text_from_doc(file_path)

        if text.strip():
            documents.append(text)
            metadatas.append({"type":"resume","filename":file})
            ids.append(f"resume_{i}")


embeddings = model.encode(documents).tolist()


collection.add(
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings,
    ids=ids
)

print(f"✅ Stored {len(documents)} resumes from .docx files in ChromaDB.")


    

