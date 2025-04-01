Smart Resume Screener is an AI-powered tool that compares a candidate's resume with a job description using LLMs, embeddings, and LangChain — providing detailed insights, match scores, and improvement suggestions.

🚀 Features

- Upload your resume (PDF)
- Paste a job description
- Get AI-based similarity score and insights
- Identifies missing skills or weak areas
- Built with LangChain, FAISS, and OpenAI's LLM
- Streamlit UI for easy use

🧰 Tech Stack

- **Python 3.10+**
- **LangChain** for LLM chains and embeddings
- **OpenAI GPT (via langchain-openai)**
- **FAISS** for vector similarity search
- **PyMuPDF** to extract PDF text
- **Streamlit** for the UI

📦 Installation

```bash
git clone https://github.com/T-ABISHEK/Smart-Resume-Screener.git
cd Smart-Resume-Screener
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

🔐 Setup

Create a `.env` file in the root directory with your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

🖥️ Run with Streamlit UI

```bash
streamlit run app.py
```

Then open the URL shown in terminal (usually `http://localhost:8501`)

---

🌟 Star this repo if you like it!
