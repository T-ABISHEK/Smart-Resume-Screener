from langchain_community.vectorstores import FAISS
from .embedder import get_embedder

def get_similarity_score(resume_text, jd_text):
    embeddings = get_embedder()
    vectorstore = FAISS.from_texts([resume_text], embedding=embeddings)
    result = vectorstore.similarity_search(jd_text, k=1)
    return result[0].page_content
