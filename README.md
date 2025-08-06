# SproutsAI Candidate Matcher

A Streamlit-based web app that recommends the best candidates for a job based on semantic relevance.

This tool was built as a take-home assignment for the Machine Learning Engineer Internship at SproutsAI.

---

## ✅ Features

- Accepts a **job description** as text input
- Accepts **multiple resumes**:
  - Upload `.pdf` or `.docx` files
  - Paste raw resume text
- Generates sentence embeddings using `all-MiniLM-L6-v2` (via `sentence-transformers`)
- Calculates **cosine similarity** between job and each resume
- Displays the **top 10 most relevant candidates**
- **BONUS**: Generates a brief **AI summary** using Hugging Face's `flan-t5-small` (runs locally without API keys)

---

## 💻 Demo Screenshot

![screenshot](screenshot.png)  <!-- Optional: Add if you have one -->

---

## 🛠️ Installation Instructions

### 1. Clone or unzip the project

```bash
cd sproutsai
