# 🎬 Movie Recommendation System using Machine Learning

This project is a **Python-based movie recommendation system** built using **Streamlit** for the user interface and **machine learning** for content-based filtering. It allows users to discover movies in three different ways:

- ✅ Find movies **similar** to a given movie
- ✅ Search movies by **actor name**
- ✅ Search movies by **director name**

---

## 🚀 Live Demo

> 🛠️ Not deployed yet. This app can be run locally using Streamlit (see below).

> 🔜 Planning to deploy on [Streamlit Cloud](https://share.streamlit.io/) soon!

---

## 🧠 How It Works

- The system uses a **cosine similarity matrix** to find similar movies.
- Data is preprocessed and stored in `.pkl` files for quick access.
- `difflib` is used for **fuzzy matching** of user input to handle typos or partial names.
- The front end is built with **Streamlit**, making it easy to run locally or online.

---

## 📦 Files Included

| File | Description |
|------|-------------|
| `app.py` / `movie_recom_app.py` | Main Python file to launch the Streamlit app |
| `movie_data.pkl` | Pickled DataFrame containing movie titles, cast, and director |
| `similarity_matrix.pkl` | Pickled similarity scores between movies |
| `movies.csv` | Original dataset used for generating the similarity matrix |
| `requirement.txt` | Python dependencies for the project |

---

## 🔧 How to Run the Project Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/movie-recommender.git
   cd movie-recommender
   pip install -r requirement.txt
   streamlit run app.py
