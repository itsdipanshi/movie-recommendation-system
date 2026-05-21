# ?? Movie Recommendation System

A content-based Movie Recommendation System built using Python, Pandas, NLP, Scikit-learn, and Streamlit.

---

## ?? Project Overview

This project recommends movies similar to the one selected by the user.

The recommendation engine uses:

* Natural Language Processing (NLP)
* Cosine Similarity
* Movie metadata such as:

  * genres
  * keywords
  * cast
  * crew
  * overview

The web application is built using Streamlit.

---

## ?? Features

* Movie recommendation engine
* Clean Streamlit user interface
* Content-based filtering
* NLP preprocessing and stemming
* Cosine similarity model
* GitHub portfolio project

---

## ??? Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle

---

## ?? Project Structure

```bash
Movie-Recommendation-System/
¦
+-- app.py
+-- movie_recommender.ipynb
+-- movies.pkl
+-- .gitignore
+-- data/
¦   +-- tmdb_5000_movies.csv
¦   +-- tmdb_5000_credits.csv
```

---

## ?? How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/itsdipanshi/movie-recommendation-system.git
```

### 2. Open Project Folder

```bash
cd movie-recommendation-system
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit App

```bash
streamlit run app.py
```

---

## ?? Output

The application allows users to:

* select a movie
* get top 5 similar movie recommendations
* interact with a clean UI

---

## ?? Future Improvements

* Add movie posters using TMDB API
* Netflix-style UI
* Deploy online using Streamlit Cloud
* Add genre filtering
* Add trending movies section

---

## ????? Author

Dipanshi

GitHub: [https://github.com/itsdipanshi](https://github.com/itsdipanshi)
