import streamlit as st
import pandas as pd
from views import View
import time

class VisualizarEstadosUI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Visualizar Estados")
        tab1, tab2 = st.tabs(["Lista", "População"])
        with tab1: VisualizarEstadosUI.lista()
        with tab2: VisualizarEstadosUI.populacao()

    def lista():
        Estados = View.estado_listar()

        text_search = st.text_input("Pesquisar estados", value="")
        
        if st.button('Pesquisar'):
            if text_search != "":
                text_search = View.estado_pesquisar(text_search)
                if len(text_search) > 0:
                    df2 = pd.DataFrame(text_search)
                    st.dataframe(df2)
                else:
                    st.error('Nenhuma correspondência encontrada.')
                    time.sleep(2)
                    st.rerun()

        st.divider()

        if len(Estados) == 0: 
            st.write("Nenhum estado cadastrado")
        else:    
            dic = []
            for obj in Estados: dic.append(obj.to_dict())
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def populacao():
        Estados = View.estado_listar()

        dic = []
        for obj in Estados:
            dic.append(obj.to_dict())   

        lista_estados = {}
        
        for x in Estados:
            n = x.get_nome()
            p = int(x.get_populacao())
            lista_estados[n] = p
        
        ordenada = dict(sorted(lista_estados.items(), key=lambda item: item[1], reverse=False))

        chaves = ordenada.keys()
        valores = ordenada.values()
        valores2 = sorted(valores)

        dados = {"Estados": chaves, "População": valores2}
        
        df = pd.DataFrame(dados).set_index("Estados")

        st.title("Estados com maior população")

        st.bar_chart(df, color='#f0f0f0')

        for x in Estados:
            dic.append(x.to_dict())


        st.divider()


        st.header('Somar população em um estado')

        op = st.selectbox("Somar populações do Estado", dic)
        id = op["ID"]
        
        if st.button('Somar'):
            st.write(View.somar_estado(id, []))

        st.divider()
    
        st.header('Somar população de estados')

        list = []

        ninputs = st.number_input('Número de estados', step=1, min_value=1)
        st.write('Numero de estados ', ninputs)

        for i in range(ninputs):
            input_values = st.selectbox(f"Estado {i+1}", dic)
            list.append(input_values) 
                
        if st.button("Adicionar", key="button_update"):
            df = pd.DataFrame(list)
            st.dataframe(df)
            st.write(f'População somada: ', View.somar_estado('', list))