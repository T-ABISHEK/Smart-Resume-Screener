import streamlit as st
from dotenv import load_dotenv
import os
import tempfile
from resume_screener.loader import load_resume_text
from resume_screener.scorer import get_similarity_score
from resume_screener.analyzer import analyze_fit

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=dotenv_path)

st.set_page_config(page_title="Smart Resume Screener", layout="centered")
st.title("📄 Smart Resume Screener")
st.markdown("Compare your resume with a job description using AI.")

resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste the job description here")

if st.button("Analyze Resume"):
    if not resume_file or not jd_text.strip():
        st.warning("Please upload a resume and paste a job description.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(resume_file.read())
            resume_path = tmp.name

        with st.spinner("Analyzing..."):
            resume_text = load_resume_text(resume_path)
            similar = get_similarity_score(resume_text, jd_text)
            result = analyze_fit(resume_text, jd_text)

        st.subheader("📊 LLM Analysis")
        st.json(result.content)
