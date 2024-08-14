import streamlit as st
from players import Player
from helpers import create_sidebar, reset_players_list, reset_input_text
from datetime import datetime
import json
import pickle

@st.dialog("Add dice")
def add_dado(this_player):
    cols = st.columns(3)

    with cols[0]:
        resource = st.radio("What resource:", options=["madeira", "barro", "ovelha", "trigo", "ferro"])
    with cols[0]:
        dado = st.radio("What dado:", options=[1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12])
    with cols[0]:
        amount = st.radio("Amount:", options=[1, 2], index=0)

    if st.button('Adidionar dado', key=f"add dado final{this_player.ID}"):
        for i in range(amount):
            this_player.dados_dict[dado].append(resource)
        st.rerun()

def roll_dice(dice):
    for player in st.session_state.players:
        for resouce in player.dados_dict[dice]:
            player.resources[resouce] = player.resources[resouce] + 1

    st.rerun()

st.set_page_config(layout="wide")

create_sidebar()

if 'players' not in st.session_state:
    reset_players_list()

if st.button("Reset players"):
    reset_players_list()

cols = st.columns(6)

for i, col in enumerate(cols):
    with col:
        if st.button(f"Dado {i+1}"):
            roll_dice(i+1)

cols = st.columns(6)
for i, col in enumerate(cols):
    with col:
        if st.button(f"Dado {i+7}"):
            roll_dice(i+7)


if len(st.session_state.players) > 0:
    for this_player in st.session_state.players:
        with st.container(border=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Name:")
            with col2:
                st.write(this_player.name)
            with col3:
                this_player.add_clear_button()

            # FOr each resource we create a 3 cols
            # name : amount: - +
            for resource in ["madeira", "barro", "ovelha", "trigo", "ferro"]:

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f'{resource.capitalize()}: ')

                with col2:
                    st.write(this_player.resources[resource])

                with col3:
                    col_minus, col_plus = st.columns(2)

                    # For each resource we create a plus and minus button
                    with col_minus:
                        this_player.add_minus(resource)
                    with col_plus:
                        this_player.add_plus(resource)
            
            # The quick buttons
            col_road, col_village, col_city, col_dc,col_dice =  st.columns(5)

            with col_road:
                this_player.add_road_button()
            with col_village:
                this_player.add_village_button()
            with col_city:
                this_player.add_city_button()
            with col_dc:
                this_player.add_dc_button()
            with col_dice:
                if st.button("Add dado", key=f"add_dado_{this_player.ID}"):
                    add_dado(this_player)
else:
    st.write("No players yet")
