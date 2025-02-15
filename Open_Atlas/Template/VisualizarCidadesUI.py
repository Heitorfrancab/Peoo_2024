import streamlit as st
import pandas as pd
from views import View
import time

class VisualizarCidadesUI:
    def main():
        Cidades = View.cidade_listar()
        if len(Cidades) == 0: 
            st.write("Nenhuma cidade cadastrada")
        else:    
            dic = []
            for obj in Cidades: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)