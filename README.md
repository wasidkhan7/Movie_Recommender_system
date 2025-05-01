# 🎬 Content-Based Movie Recommender System

This project is a **Content-Based Filtering Movie Recommender System** built using Python and Streamlit. It recommends the top 5 similar movies based on the plot/description of a selected movie.

---

## 🚀 Features

- ✅ Recommends top 5 similar movies based on selected title
- ✅ Uses **content-based filtering**
- ✅ Implements **text preprocessing**: lowercasing, removing stopwords, punctuation, stemming
- ✅ Uses **TF-IDF Vectorization**
- ✅ Calculates **Cosine Similarity** between movie plots
- ✅ Displays movie **posters** using TMDb API
- ✅ Deployed with **Streamlit** web interface

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas
- Scikit-learn
- NLTK
- Streamlit
- Requests
- TMDb API

---

## 📂 Project Structure


---

## 📚 Content-Based Filtering Workflow

1. **Preprocessing Movie Descriptions**
   - Combine important features (title, overview, genres, keywords, cast, crew)
   - Clean text: remove punctuation, lowercase, remove stopwords
   - Apply **stemming** using NLTK's PorterStemmer

2. **Text Vectorization**
   - Use **CountVectorizer** to convert text to vectors

3. **Similarity Calculation**
   - Use **Cosine Similarity** to find similar movie vectors

4. **Recommender Function**
   - Takes a movie title as input
   - Returns the top 5 similar movies using the similarity matrix

5. **Poster Fetching**
   - Movie posters fetched using TMDb API based on movie title

---

## 💻 Streamlit App UI

- Dropdown menu to select a movie
- "Recommend" button
- Displays 5 movie recommendations with poster and title

---
![image](https://github.com/user-attachments/assets/10729f3d-0d1e-4f97-a8da-e18b32339045)




