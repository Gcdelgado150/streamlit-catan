import streamlit as st
from helpers import create_sidebar
import os
import pickle

# Define a function to load the game state from a pickle file
def load_game(filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)  # Deserialize
            for k, v in data.items():
                st.session_state[k] = v
        st.success("Successfully loaded game state.")
    except Exception as e:
        st.error(f"Error loading game state: {e}")

create_sidebar()

# List .pkl files in the directory
files = [f for f in os.listdir("games_played/") if f.endswith('.pkl')]
st.write(files)

# Dropdown menu for selecting a game
selected = st.selectbox(
    label="Choose the game...", 
    options=files,
    index=None,
    placeholder="Choose an option"
)

# Display the contents of the selected pickle file
if selected:
    with st.expander("Previous game:"):
        try:
            with open(f'games_played/{selected}', 'rb') as f:
                d = pickle.load(f)  # Deserialize
                st.write(d)  # Display the contents
        except Exception as e:
            st.error(f"Error reading file: {e}")

# Load the selected game state into session state when the button is clicked
if st.button("Select game") and selected:
    load_game(f'games_played/{selected}')