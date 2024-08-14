import streamlit as st
from datetime import datetime
import pickle
import os

def save_game_state():
    now = datetime.now()
    filename = f"games_played/game_{now.strftime('%Y_%m_%d_%H_%M_%S_%f')}.pkl"  # Adding time for uniqueness

    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Ensure directory exists

    try:
        with open(filename, 'wb') as f:
            pickle.dump(dict(st.session_state), f)  # Serialize the session state dict
        st.success(f"File saved to {filename}")
    except Exception as e:
        st.error(f"Error saving file: {e}")
    
def create_sidebar():
    # Clear the sidebar
    st.sidebar.title("Catan")
    st.sidebar.page_link("home.py", label="Inicio") 
    st.sidebar.page_link("pages/player_creation.py", label="Players Creation")

    st.sidebar.divider()
    st.sidebar.page_link("pages/load_game.py", label="Load Game")

    st.sidebar.divider()
    if st.sidebar.button("Save game"):
        save_game_state()