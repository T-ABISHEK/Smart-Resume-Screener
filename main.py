import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path=dotenv_path)

print("🔑 API Key from .env:", os.getenv("OPENAI_API_KEY"))  

from resume_screener.loader import load_resume_text
from resume_screener.scorer import get_similarity_score
from resume_screener.analyzer import analyze_fit

if __name__ == '__main__':
    resume_text = load_resume_text("sample_resume.pdf")
    with open("job_description.txt", "r") as f:
        jd_text = f.read()

    similar_resume = get_similarity_score(resume_text, jd_text)
    analysis = analyze_fit(resume_text, jd_text)

    print("\n--- Similar Resume Chunk ---\n", similar_resume)
    print("\n--- LLM Analysis ---\n", analysis)
