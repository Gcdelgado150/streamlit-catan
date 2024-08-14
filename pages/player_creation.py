import streamlit as st
from helpers import create_sidebar, reset_players_list, reset_input_text
from players import Player

st.write(st.session_state)
if 'players' not in st.session_state:
    reset_players_list()
else:
    for player in st.session_state.players:
        st.write(player.name)
if 'input_text' not in st.session_state:
    reset_input_text()
if 'disabled1' not in st.session_state:
    st.session_state.disabled1 = False
if 'disabled2' not in st.session_state:
    st.session_state.disabled2 = False
if 'disabled3' not in st.session_state:
    st.session_state.disabled3 = False

create_sidebar()

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        new_player1 = st.text_input('Novo jogador:', 
                                    key="p1", 
                                    value=st.session_state.input_text)

        if st.button("Novo Player 1", disabled=st.session_state.disabled1) and new_player1:
            st.session_state.disabled1 = True
            st.session_state.players.append(Player(name=new_player1))
            st.rerun()
with col2:
    with st.container(border=True):
        new_player2 = st.text_input('Novo jogador:', 
                                    key="p2", 
                                    value=st.session_state.input_text)

        if st.button("Novo Player 2", disabled=st.session_state.disabled2) and new_player2:
            st.session_state.disabled2 = True
            st.session_state.players.append(Player(name=new_player2))
            st.rerun()
with col3:
    with st.container(border=True):
        new_player3 = st.text_input('Novo jogador:', 
                                    key="p3", 
                                    value=st.session_state.input_text)

        if st.button("Novo Player 3", disabled=st.session_state.disabled3) and new_player3:
            st.session_state.disabled3 = True
            st.session_state.players.append(Player(name=new_player3))
            st.rerun()