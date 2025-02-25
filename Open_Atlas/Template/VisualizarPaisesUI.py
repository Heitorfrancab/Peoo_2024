import streamlit as st
import pandas as pd
from views import View
import time

class VisualizarPaisesUI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Visualizar Países")
        tab1, tab2 = st.tabs(["Lista", "População"])
        with tab1: VisualizarPaisesUI.lista()
        with tab2: VisualizarPaisesUI.populacao()
    
    def lista():
        Paises = View.pais_listar()

        text_search = st.text_input("Pesquise países", value="")
        
        if st.button('Pesquisar'):
            if text_search != "":
                text_search = View.pais_pesquisar(text_search)
                if len(text_search) > 0:
                    df2 = pd.DataFrame(text_search)
                    st.dataframe(df2)
                else:
                    st.error('Nenhuma correspondência encontrada.')
                    time.sleep(2)
                    st.rerun()

        st.divider()

        if len(Paises) == 0: 
            st.write("Nenhum país cadastrado")
        else:    
            dic = []
            for obj in Paises: dic.append(obj.to_dict())
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def populacao():
        Paises = View.pais_listar()
        dic = []
        for obj in Paises:
            dic.append(obj.to_dict())   

        lista_paises = {}
        
        for x in Paises:
            n = x.get_nome()
            p = int(x.get_populacao())
            lista_paises[n] = p
        
        ordenada = dict(sorted(lista_paises.items(), key=lambda item: item[1], reverse=False))

        chaves = ordenada.keys()
        valores = ordenada.values()
        valores2 = sorted(valores)

        dados = {"Países": chaves, "População": valores2}
        
        df = pd.DataFrame(dados).set_index("Países")

        st.title("Países com maior população")

        st.bar_chart(df, color='#f0f0f0')

        st.divider()


        st.header('Somar população em um país')

        op = st.selectbox("Somar populações de um país", dic)
        id = op["ID"]
        
        if st.button('Somar'):
            st.write(View.somar_pais(id, []))

        st.divider()
    
        st.header('Somar população de países')

        list = []

        ninputs = st.number_input('Número de países', step=1, min_value=1)
        st.write('Numero de países ', ninputs)

        for i in range(ninputs):
            input_values = st.selectbox(f"País {i+1}", dic)
            list.append(input_values) 
                
        if st.button("Adicionar", key="button_update"):
            df = pd.DataFrame(list)
            st.dataframe(df)
            st.write(f'População somada: ', View.somar_pais('', list))