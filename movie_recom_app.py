import pickle
import streamlit as st
import pandas as pd
import difflib

# ----------------------------
# Load Data
# ----------------------------
movie_data = pickle.load(open(r'C:\Users\875dh\OneDrive\Desktop\New folder\ML\Mini Project\movie_data.pkl', 'rb'))
similarity_matrix = pickle.load(open(r'C:\Users\875dh\OneDrive\Desktop\New folder\ML\Mini Project\similarity_matrix.pkl', 'rb'))

# ----------------------------
# Helper Functions
# ----------------------------

def get_close_match(user_input, options_list):
    match = difflib.get_close_matches(user_input, options_list)
    return match[0] if match else None

def recommended_movies(movie_name, top_n=10):
    movie_list = movie_data['title'].tolist()
    close_match = get_close_match(movie_name, movie_list)
    if not close_match:
        return ["❌ No close match found for the movie."]
    
    index = movie_data[movie_data['title'] == close_match].index[0]
    similarity_scores = list(enumerate(similarity_matrix[index]))
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    return [movie_data.iloc[i[0]]['title'] for i in sorted_movies]

def find_movies_by_director(director_name):
    df = movie_data[movie_data['director'].str.lower() == director_name.lower()]
    
    if df.empty:
        all_directors = movie_data['director'].dropna().unique().tolist()
        close_match = get_close_match(director_name, all_directors)
        if not close_match:
            return ["❌ No movies found for the given director."]
        df = movie_data[movie_data['director'] == close_match]

    return df['title'].tolist()[:20]

def find_movies_by_actor(actor_name):
    df = movie_data.dropna(subset=['cast'])
    matched = df[df['cast'].str.lower().str.contains(actor_name.lower())]

    if matched.empty:
        actor_set = set()
        for cast in df['cast']:
            for actor in cast.split(','):
                actor_set.add(actor.strip())
        close_match = get_close_match(actor_name, list(actor_set))
        if not close_match:
            return ["❌ No movies found for the given actor."]
        matched = df[df['cast'].str.contains(close_match, case=False)]

    return matched['title'].tolist()[:20]

# ----------------------------
# Streamlit UI
# ----------------------------

st.set_page_config(page_title="🎬 Movie Explorer", layout="centered")
st.title("🎥 Movie Recommendation System")

choice = st.selectbox(
    "Choose an option:",
    ("Recommend similar movies", "Find movies by actor", "Find movies by director")
)

user_input = st.text_input('Enter the movie / actor / director name:')

if st.button("Search"):
    if user_input.strip() == '':
        st.warning("⚠️ Please enter a valid name.")
    else:
        st.subheader("🔍 Results:")
        if choice == "Recommend similar movies":
            results = recommended_movies(user_input)
        elif choice == "Find movies by actor":
            results = find_movies_by_actor(user_input)
        elif choice == "Find movies by director":
            results = find_movies_by_director(user_input)
        
        if results:
            for i, title in enumerate(results, 1):
                st.write(f"{i}. {title}")
        else:
            st.info("No results found.")
