# 🧠 Candidate Recommendation Engine — SproutsAI Take-Home Assignment

A web app that recommends the **most relevant candidates** for a given job description using semantic similarity and AI-powered summaries.

Built as part of the take-home assignment for the **SproutsAI Machine Learning Engineer Internship**.

---

## 🚀 Public App Link
👉 [https://mrunalikatta1998-candidate-recommendation-engine.streamlit.app](https://mrunalikatta1998-candidate-recommendation-engine.streamlit.app)

No login required. Paste job description + resumes → get AI-ranked matches and summaries.

---

## 🧩 Features Implemented
- 📥 Accept job description (text input)
- 📂 Accept multiple resumes (PDF or plain text)
- 🤖 Generate embeddings using `sentence-transformers`
- 📐 Compute **cosine similarity** between job and resumes
- 🏆 Display top 5–10 relevant candidates (name + similarity)
- 🧠 BONUS: Generate smart AI summaries using **GPT-3.5 via OpenRouter**

---

## 🛠️ Tech Stack
| Layer         | Tool / Library                      |
|---------------|-------------------------------------|
| Frontend UI   | Streamlit                           |
| Embeddings    | `sentence-transformers` (MiniLM)    |
| Similarity    | Cosine similarity (`scikit-learn`)  |
| Summarization | GPT-3.5 via OpenRouter (`openai==0.28`) |
| Hosting       | Streamlit Cloud                     |

---

## ✅ My Approach
- Used MiniLM model from `sentence-transformers` for light-weight embeddings
- Used `PyPDF2` and `python-docx` to extract text from uploaded resumes
- Matched job ↔ resumes using cosine similarity of embeddings
- Integrated GPT-3.5 via OpenRouter to generate 2-line summaries on why a resume is (or isn’t) a good fit
- Used `.streamlit/secrets.toml` to keep API keys secure

---

## 🧠 Assumptions
- Resumes will be either PDFs or pasted text
- One job description is matched against many candidates at once
- Summaries use 2500-character max chunk from resumes
- Free-tier OpenRouter GPT-3.5 is used for bonus feature
- Similarity threshold not enforced — sorted by cosine distance only


---

## 📁 Project Structure
```
Candidate-Recommendation-Engine/
├── app.py                  # Main Streamlit app
├── utils.py                # PDF/DOCX parsing
├── requirements.txt        # All dependencies
├── .gitignore              # Ignore secrets, venv, cache
└── .streamlit/
    └── secrets.toml        # Secure OpenRouter key (excluded from Git)
```

---

## 🧪 Run Locally
```bash
# 1. Create and activate virtual env
python -m venv venv310
venv310\Scripts\activate

# 2. Install required packages
pip install -r requirements.txt

# 3. Add your API key to .streamlit/secrets.toml

# 4. Start the app
streamlit run app.py
```

---

## 👩‍💻 Developed By
**Mrunali Katta**  
🔗 [GitHub Profile](https://github.com/mrunalikatta1998)

---

✅ Designed specifically for SproutsAI Take-Home Evaluation
