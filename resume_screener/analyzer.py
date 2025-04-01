from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load .env safely
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not found. Please check your .env")

llm = ChatOpenAI(temperature=0, api_key=api_key)

prompt = PromptTemplate.from_template("""
Compare the following resume and job description.

Resume:
{resume}

Job Description:
{jd}

Respond with:
- Match score (0-100%)
- 3-5 missing/weak areas
- 2-line summary
Format your response in JSON.
""")

chain = prompt | llm

def analyze_fit(resume, jd):
    return chain.invoke({"resume": resume, "jd": jd})
