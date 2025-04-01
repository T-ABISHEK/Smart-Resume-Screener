from langchain_community.document_loaders import PyMuPDFLoader

def load_resume_text(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    docs = loader.load()
    return docs[0].page_content
