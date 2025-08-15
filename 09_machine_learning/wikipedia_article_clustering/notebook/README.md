# Wikipedia Article Clustering & Recommender System using NMF

## 📌 Project Overview
This project demonstrates **Unsupervised Learning** techniques for clustering Wikipedia articles and extending it into a **content-based recommender system** using **Non-negative Matrix Factorization (NMF)**.  
We use **TF-IDF** to transform textual data into numerical features and apply NMF to extract latent topics. The recommender system suggests similar articles based on learned topics.

---

## 📂 Dataset
We use a subset of Wikipedia articles fetched using `scikit-learn`'s `fetch_20newsgroups` dataset for demonstration.  
- Each article is represented as a document in a sparse matrix.  
- The dataset is transformed using **TF-IDF Vectorization** to weight important terms.

---

## ⚙️ Key Steps Implemented

### **1. Data Loading**
- Load textual Wikipedia-style articles (or 20 Newsgroups as a proxy dataset).
- Preprocess data to remove stop words and perform tokenization.

### **2. TF-IDF Transformation**
- Convert raw text into TF-IDF matrix to emphasize important terms.
- Use `TfidfVectorizer` from scikit-learn.

### **3. Dimensionality Reduction with NMF**
- Apply **Non-negative Matrix Factorization** to discover hidden topics.
- Each article is represented as a combination of latent topics.

### **4. Article Clustering**
- Group articles into topics based on NMF components.
- Display top words per topic to interpret themes.

### **5. Recommender System (Extension)**
- Create a function to recommend articles similar to a given one.
- Measure similarity in **topic space** using cosine similarity.

---

## 📌 Real-World Applications

# News article recommendation

# Research paper suggestion

# E-commerce product recommendation based on descriptions
