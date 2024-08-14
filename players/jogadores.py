import streamlit as st

class Player():
    def __init__(self, name=None, madeira=0, barro=0, ovelha=0, trigo=0, ferro=0):
        self.ID = len(st.session_state.players) + 1

        self.name = name
        self.resources = {
            "madeira": madeira,
            "barro": barro,
            "ovelha": ovelha,
            "trigo": trigo,
            "ferro": barro,
                          }

        self.dados = []
        self.dados_dict = {1: [], 
                           2: [], 
                           3: [], 
                           4: [], 
                           5: [], 
                           6: [], 
                           7: [], 
                           8: [], 
                           9: [], 
                           10: [], 
                           11: [], 
                           12: []}

    def add_plus(self, resource):
        if st.button(f":heavy_plus_sign:", key=f"+ {self.ID} {resource}"):
            self.resources[resource] = self.resources[resource] + 1
            st.rerun()

    def add_minus(self, resource):
        if st.button(f":heavy_minus_sign:", key=f"- {self.ID} {resource}"):
            self.resources[resource] = self.resources[resource] - 1
            st.rerun()

    def add_clear_button(self):
        if st.button(f"Clear {self.ID}", key=f"Clear {self.ID}"):
            self.resources["madeira"] = 0
            self.resources["barro"] = 0
            self.resources["ovelha"] = 0
            self.resources["trigo"] = 0
            self.resources["ferro"] = 0
            st.rerun()

    def add_road_button(self):
        if st.button(f"Build Road {self.ID}", key=f"Road {self.ID}"):
            self.resources["madeira"] = self.resources["madeira"] - 1
            self.resources["barro"] = self.resources["barro"] - 1
            st.rerun()

    def add_village_button(self):
        if st.button(f"Build Village {self.ID}", key=f"Village {self.ID}"):
            self.resources["madeira"] = self.resources["madeira"] - 1
            self.resources["barro"] = self.resources["barro"] - 1
            self.resources["ovelha"] = self.resources["ovelha"] - 1
            self.resources["trigo"] = self.resources["trigo"] - 1
            st.rerun()

    def add_city_button(self):
        if st.button(f"Build City {self.ID}", key=f"City {self.ID}"):
            self.resources["ovelha"] = self.resources["ovelha"] - 2
            self.resources["trigo"] = self.resources["trigo"] - 3
            st.rerun()

    def add_dc_button(self):
        if st.button(f"Buy DC {self.ID}", key=f"DC {self.ID}"):
            self.resources["ovelha"] = self.resources["ovelha"] - 1
            self.resources["trigo"] = self.resources["trigo"] - 1
            self.resources["ferro"] = self.resources["ferro"] - 1
            st.rerun()


        
