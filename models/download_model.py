from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
model.save("models/all-MiniLM-L6-v2")

print("✅ Model downloaded and saved to models/all-MiniLM-L6-v2")
