import streamlit as st
import pickle

# Load files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #141414;
        color: white;
    }

    .stButton>button {
        background-color: #E50914;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        border: none;
    }

    .stSelectbox label {
        color: white !important;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
# Custom Heading
st.markdown(
    """
    <h1 style='text-align: center; color: #E50914;'>
        🎬 Movie Recommendation System
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align: center;'>
        Find movies similar to your favorites
    </h4>
    """,
    unsafe_allow_html=True
)

# Movie list
movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie",
    movie_list
)

# Recommendation function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# Button
if st.button('Recommend'):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(
            f"""
            <div style='padding:15px;
                        border-radius:10px;
                        background-color:#262730;
                        text-align:center;
                        color:white;'>
                <h4>{recommendations[0]}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div style='padding:15px;
                        border-radius:10px;
                        background-color:#262730;
                        text-align:center;
                        color:white;'>
                <h4>{recommendations[1]}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div style='padding:15px;
                        border-radius:10px;
                        background-color:#262730;
                        text-align:center;
                        color:white;'>
                <h4>{recommendations[2]}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div style='padding:15px;
                        border-radius:10px;
                        background-color:#262730;
                        text-align:center;
                        color:white;'>
                <h4>{recommendations[3]}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            f"""
            <div style='padding:15px;
                        border-radius:10px;
                        background-color:#262730;
                        text-align:center;
                        color:white;'>
                <h4>{recommendations[4]}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )