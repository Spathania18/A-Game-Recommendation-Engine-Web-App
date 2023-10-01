# importing libraries
import pickle
import streamlit as st 
import requests

# Creating recommend function to find games
def recommend(game):
    index = games[games['Title'] == game].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x: x[1])
    recommended_games_names = []
    for i in distance[1:4]:
        recommended_games_names.append(games.iloc[i[0]].Title)
    return recommended_games_names

# Giving heading to the app
st.header("Game Recommendation System")

# Loading Pickle files
games = pickle.load(open("essentials/game_list.pkl", "rb"))
                    
similarity = pickle.load(open("essentials/similarity.pkl", "rb"))

# Making a list of titles for dropdown bar
games_list = games['Title'].values

# Creating a dropdown box to select/enter value
selected_game = st.selectbox(
    "Type or Select a game",
    games_list
)

# initializing and Providing Functionality to the select box button

if st.button('Show Games'):
    recommend_game_names = recommend(selected_game)
    col1, col2, col3 = st.columns(3)  # creating variables to store recommended values

    with col1:
        st.text(recommend_game_names[0])
    with col2:
        st.text(recommend_game_names[1])
    with col3:
        st.text(recommend_game_names[2])