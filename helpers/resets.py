import streamlit as st

def reset_players_list():
    st.session_state.players = []
    
def reset_input_text():
    st.session_state.input_text = None