# AI Semantic Search Engine
**Multimodal Text–Image Retrieval using CLIP & FAISS**

## 📌 Overview
This project implements an AI-powered semantic search engine that enables **text-based image retrieval** using deep learning embeddings.  
It leverages **OpenAI CLIP** for multimodal understanding and **FAISS** for efficient vector similarity search.

The project supports:
- A **CLI-based semantic search application**
- A modular structure for indexing and search logic

---

## 🧠 Key Features
- Semantic text-to-image search
- CLIP-based embedding generation
- FAISS-powered vector similarity search
- Lightweight and efficient Python implementation
- Prebuilt index support for faster startup

---

## 🛠 Tech Stack
- Python
- CLIP (OpenAI)
- FAISS
- PyTorch
- Pillow
- NumPy

---


## ⚙️ How It Works
1. Images are converted into vector embeddings using CLIP  
2. Embeddings are indexed using FAISS  
3. A user enters a text query in the CLI  
4. The query embedding is matched against indexed image vectors  
5. The most semantically similar image paths are returned  

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ (Optional) Build FAISS Index
```bash
python faiss_index_builder.py
```

### 3️⃣ Run Semantic Search
```bash
python app.py
```

Type a text query in the terminal to retrieve matching images.
---

## 📈 Use Cases
- AI-powered image search
- Visual content discovery
- Semantic retrieval systems
- Recommendation engines





