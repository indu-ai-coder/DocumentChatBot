import streamlit as st
import chromadb
from openai import OpenAI
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
chroma = chromadb.Client()
collection = chroma.get_or_create_collection("user_docs")
st.title("📚 Chat with Your Documents - Powered by RAG 🧠")
st.write("Upload a PDF, then ask questions about it!")
# --- Step 1: Upload PDF ---
uploaded_file = st.file_uploader("Upload your document", type=["pdf"])
if uploaded_file:
    pdf = PdfReader(uploaded_file)
    text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    st.success("✅ Document uploaded and text extracted!")
    
    # --- Step 2: Create Embeddings and Store in Vector DB ---
    st.write("Creating embeddings and storing in database... please wait ⏳")
    for i, chunk in enumerate(text.split(". ")):
        if chunk.strip():
            embedding = client.embeddings.create(
                input=chunk, model="text-embedding-3-small"
            ).data[0].embedding
            collection.add(ids=[f"chunk_{i}"], embeddings=[embedding], documents=[chunk])
    st.success("✅ Document indexed successfully!")
# --- Step 3: Ask a Question ---
query = st.text_input("Ask a question about your document:")
if query:
    query_embedding = client.embeddings.create(
        input=query, model="text-embedding-3-small"
    ).data[0].embedding
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    context = " ".join(results["documents"][0])
    prompt = f"Use the following context to answer:\n\n{context}\n\nQuestion: {query}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    st.markdown("### 🤖 Answer:")
    st.write(response.choices[0].message.content)