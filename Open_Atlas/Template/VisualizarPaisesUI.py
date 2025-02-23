import streamlit as st
import pandas as pd
from views import View
import time

class VisualizarPaisesUI:
    def main():
        Paises = View.pais_listar()
        if len(Paises) == 0: 
            st.write("Nenhum país cadastrado")
        else:    
            dic = []
            for obj in Paises: dic.append(obj.to_dict())
            df = pd.DataFrame(dic)
            st.dataframe(df)