# Vector Store

A **Vector Store** is a system designed to store and retrieve data represented as numerical vectors.

---

## 🔑 Key Features

1. **Vector + Metadata Storage**  
   Stores vectors along with associated metadata  
   _Example: movie vectors with metadata like plot, movie ID_

2. **Types of Storage**  
   - **In-Memory (RAM)**  
   - **On-Disk (Hard Drive)**

3. **Similarity Search**  
   Enables searching for vectors that are most similar to a given query vector

4. **Indexing**  
   Efficient indexing mechanism for large vector sets  
   _Example: For 10 lakh vectors →_
   - Create 10 clusters
   - Compute average vector per cluster → **centroid**
   - Result: 10 centroid vectors
     - a. Compare query vector with centroid vectors
     - b. Select the cluster with the closest similarity for focused search

5. **CRUD Operations**  
   Supports basic Create, Read, Update, Delete operations on vector data

---

## 🚀 Use Cases

1. **Semantic Search**  
   Retrieve results based on meaning instead of keywords

2. **RAG (Retrieval-Augmented Generation)**  
   Improves response quality of LLMs by grounding them in retrieved data

3. **Recommender Systems**  
   Suggest items (movies, products, etc.) based on vector similarity

4. **Image/Multimedia Search**  
   Search similar images, videos, or audio using vector representations

