import streamlit as st
import cohere

from utils import extract_text_from_pdf, extract_text_from_docx
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load Cohere API key from secrets
cohere_client = cohere.Client(st.secrets["cohere"]["api_key"])

# Load the embedding model (cached)
@st.cache_resource
def load_model():
    st.write("🔍 Loading embedding model...")
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# Use Cohere to generate AI summary
def generate_fit_summary(job_desc, resume_text):
    prompt = f"""
You are an assistant helping a recruiter.
Given the job description and candidate resume, write 1–2 sentences about why this candidate is a good fit.

Job:
{job_desc}

Resume:
{resume_text[:1500]}
"""
    try:
        response = cohere_client.generate(
            model="command",
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )
        return response.generations[0].text.strip()
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

            for match in top_matches:
                st.markdown(f"**{match['id']}** — Similarity: `{match['score']}`")
                with st.spinner("🤖 Generating AI summary..."):
                    summary = generate_fit_summary(job_description, match["text"])
                    st.markdown(f"**AI Summary:** {summary}")

        except Exception as e:
            st.error(f"🚨 Matching failed: {e}")
