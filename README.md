# 🧠 Candidate Recommendation Engine

A web application that recommends the most relevant candidates for a given job description using semantic search and AI-generated summaries.

Built using `Streamlit`, `sentence-transformers`, `scikit-learn`, and GPT-3.5 via OpenRouter API.

---

## 🚀 Live Demo

👉 [https://mrunalikatta1998-candidate-recommendation-engine.streamlit.app](https://mrunalikatta1998-candidate-recommendation-engine.streamlit.app)

No login required. Paste a job description, upload resumes (PDF/DOCX) or paste them as text, and get top-ranked matches with AI summaries.

---

## ✅ Features & Implementation

- 📝 Accepts job description via text input
- 📂 Accepts resumes in two formats:
  - Uploaded files (PDF or DOCX)
  - Pasted plain text for each candidate
- 📄 Parses resumes using `PyPDF2` and `python-docx`
- 🤖 Generates semantic embeddings with `"paraphrase-MiniLM-L6-v2"` model from `sentence-transformers`
- 📐 Computes **cosine similarity** between job and each resume
- 🏆 Displays top 10 candidates sorted by similarity score
- 🧠 For each match, generates a GPT-3.5 summary explaining the fit using OpenRouter API

---

## 🛠️ Tech Stack

| Component      | Tool / Library                        |
|----------------|----------------------------------------|
| UI             | Streamlit                              |
| Embeddings     | sentence-transformers (MiniLM model)   |
| File Parsing   | PyPDF2, python-docx                    |
| Similarity     | scikit-learn (cosine similarity)       |
| Summarization  | GPT-3.5 via OpenRouter API (openai)    |
| Hosting        | Streamlit Cloud                        |

---

## 🔍 How It Works

1. **Input**: User provides a job description and resumes (files or text).
2. **Preprocessing**: Text is extracted from PDFs or DOCX resumes.
3. **Embedding**: Job description and each resume are converted into vector embeddings using MiniLM.
4. **Matching**: Cosine similarity scores are calculated between job and each resume.
5. **Ranking**: Top 10 resumes with highest similarity are shown.
6. **Summarization**: GPT-3.5 generates a 2-line explanation for each match, stating why the candidate is (or isn’t) a good fit.

---

## 📁 Project Structure

```
candidate-recommendation-engine/
├── app.py                # Main Streamlit app logic
├── utils.py              # Functions to extract text from PDF/DOCX
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignore secrets, venv, pycache
└── .streamlit/
    └── secrets.toml      # OpenRouter API key (not committed)
```

---

## 🧪 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/mrunalikatta1998/candidate-recommendation-engine.git
cd candidate-recommendation-engine

# 2. Create a virtual environment
python -m venv venv310
venv310\Scripts\activate   # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your OpenRouter API key to .streamlit/secrets.toml

# 5. Launch the app
streamlit run app.py
```

---

## 🔐 API Key Setup

To use GPT-3.5 summarization, set up your `.streamlit/secrets.toml` file like this:

```toml
[openrouter]
api_key = "your_openrouter_api_key"
```

This file is excluded from Git using `.gitignore`.

---

## 🎥 Demo Videos

### 📂 Resume Upload Flow
<video src="https://github.com/user-attachments/assets/7fcb4a27-99aa-4469-b4bb-f28c897d06d0" controls width="100%"></video>

### 📝 Paste Resume Text Flow
<video src="https://github.com/user-attachments/assets/d8ddcdfb-ea95-4236-9545-7d4349258036" controls width="100%"></video>

---

## 👩‍💻 Author

**Mrunali Katta**  
🔗 [GitHub Profile](https://github.com/mrunalikatta1998)
