import streamlit as st
import pandas as pd
from views import View
import time

class VisualizarEstadosUI:
    def main():
        Estados = View.estado_listar()
        if len(Estados) == 0: 
            st.write("Nenhum estado cadastrado")
        else:    
            dic = []
            for obj in Estados: dic.append(obj.to_dict())
            df = pd.DataFrame(dic)
            st.dataframe(df)