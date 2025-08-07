import streamlit as st
from utils import extract_text_from_pdf, extract_text_from_docx
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import openai

# Load local embedding model (cached)
@st.cache_resource
def load_embedding_model():
    st.write("🔍 Loading embedding model...")
    return SentenceTransformer("models/all-MiniLM-L6-v2")

model = load_embedding_model()

# Configure OpenRouter (GPT-3.5 via OpenRouter)
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = st.secrets["openrouter"]["api_key"]

# Generate summary using GPT-3.5 (via OpenRouter)
def generate_fit_summary(job_desc, resume_text):
    prompt = f"""
You are an AI assistant helping a recruiter.

Job Description:
{job_desc}

Candidate Resume:
{resume_text[:2500]}

Task:
Write 1–2 sentences explaining whether this candidate is a good or bad fit for the job, and why. Be specific about relevant skills or lack of alignment.
"""
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error generating summary: {e}"

# UI title and description
st.title("🌱 SproutsAI Candidate Matcher")
st.markdown("Upload resumes OR paste resume text, and match them with a job description.")

# Step 1: Job Description Input
job_description = st.text_area("📝 Job Description", height=200)
st.write("✅ Job description received." if job_description else "❌ Waiting for job description...")

# Step 2: Resume Input Mode
input_mode = st.radio("Choose resume input method:", ["Upload Files", "Paste Text"], horizontal=True)
resume_texts = []

# File Upload Mode
if input_mode == "Upload Files":
    uploaded_files = st.file_uploader("📂 Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

    if uploaded_files:
        st.write(f"✅ {len(uploaded_files)} file(s) uploaded.")
        for file in uploaded_files:
            try:
                st.write(f"📄 Reading: {file.name}")
                if file.name.endswith(".pdf"):
                    text = extract_text_from_pdf(file)
                elif file.name.endswith(".docx"):
                    text = extract_text_from_docx(file)
                else:
                    text = ""
                if not text.strip():
                    st.warning(f"⚠️ No text extracted from {file.name}")
                resume_texts.append({"id": file.name, "text": text})
            except Exception as e:
                st.error(f"❌ Failed to read {file.name}: {e}")
    else:
        st.write("❌ No resumes uploaded.")

# Paste Text Mode
else:
    num_fields = st.number_input("How many resumes will you paste?", min_value=1, max_value=100, value=1)
    st.info("You can paste up to 100 candidate resumes below.")

    for i in range(num_fields):
        name = st.text_input(f"👤 Candidate {i+1} Name")
        text = st.text_area(f"📝 Candidate {i+1} Resume Text", height=150)
        if name and text:
            resume_texts.append({"id": name, "text": text})
        else:
            st.write(f"⚠️ Candidate {i+1} is incomplete (name/text missing)")

# Step 3: Matching Logic
if st.button("🚀 Match Candidates"):
    st.write("🧪 Starting matching process...")

    if not job_description:
        st.warning("❌ Please enter a job description.")
    elif not resume_texts:
        st.warning("❌ Please provide at least one resume.")
    else:
        try:
            st.write("🔢 Generating embeddings...")
            job_embedding = model.encode([job_description])
            resume_embeddings = model.encode([r["text"] for r in resume_texts])

            st.write("📏 Calculating cosine similarity...")
            similarities = cosine_similarity(job_embedding, resume_embeddings)[0]

            for i, sim in enumerate(similarities):
                resume_texts[i]["score"] = round(float(sim), 4)

            top_matches = sorted(resume_texts, key=lambda x: x["score"], reverse=True)[:10]

            st.subheader("🏆 Top 10 Matches")

            for i, match in enumerate(top_matches, 1):
                st.markdown(f"**{i}. {match['id']}** — Similarity: `{match['score']}`")
                with st.spinner("🤖 Generating AI summary..."):
                    summary = generate_fit_summary(job_description, match["text"])
                    st.markdown(f"**AI Summary:** {summary}")

        except Exception as e:
            st.error(f"🚨 Matching failed: {e}")
            