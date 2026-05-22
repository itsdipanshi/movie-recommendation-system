import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Sidebar
st.sidebar.title("About")
st.sidebar.info(
    """
🎬 Movie Recommendation System

This app recommends movies using
Machine Learning + NLP.

Technologies Used:
- Python
- Pandas
- Scikit-learn
- Streamlit
"""
)

# Load files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie list
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie", movie_list)

# Styling
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
st.markdown(
    "<h1 style='text-align: center; color: #E50914;'>🎬 Movie Recommendation System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align: center;'>Find movies similar to your favorites</h4>",
    unsafe_allow_html=True
)

# Recommendation function (CLEAN VERSION)
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index

    if len(movie_index) == 0:
        return []

    movie_index = movie_index[0]

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
if st.button('🎥 Show Recommendations'):

    names = recommend(selected_movie)

    st.subheader("Recommended Movies")

    if len(names) == 0:
        st.warning("No recommendations found.")
    else:
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.write(names[0])

        with col2:
            st.write(names[1])

        with col3:
            st.write(names[2])

        with col4:
            st.write(names[3])

        with col5:
            st.write(names[4])

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)
