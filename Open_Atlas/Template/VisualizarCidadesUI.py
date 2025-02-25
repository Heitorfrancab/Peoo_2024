import streamlit as st
import pandas as pd
from views import View
import time

class VisualizarCidadesUI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Visualizar Cidades")
        tab1, tab2 = st.tabs(["Lista", "População"])
        with tab1: VisualizarCidadesUI.lista()
        with tab2: VisualizarCidadesUI.populacao()
    
    def lista():
        Cidades = View.cidade_listar()
        text_search = st.text_input("Pesquisar cidades", value="")
        
        if st.button('Pesquisar'):
            if text_search != "":
                text_search = View.cidade_pesquisar(text_search)
                if len(text_search) > 0:
                    df2 = pd.DataFrame(text_search)
                    st.dataframe(df2)
                else:
                    st.error('Nenhuma correspondência encontrada.')
                    time.sleep(2)
                    st.rerun()

        st.divider()
        
        if len(Cidades) == 0: 
            st.write("Nenhuma cidade cadastrada")
        else:
            dic = []
            for obj in Cidades:
                dic.append(obj.to_dict())
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def populacao():
        Cidades = View.cidade_listar()
        dic = []
        for x in Cidades:
            dic.append(x.to_dict())

        lista_cidades = {}
        
        for x in Cidades:
            n = x.get_nome()
            p = int(x.get_populacao())
            lista_cidades[n] = p
        
        ordenada = dict(sorted(lista_cidades.items(), key=lambda item: item[1], reverse=False))

        chaves = ordenada.keys()
        valores = ordenada.values()
        valores2 = sorted(valores)

        dados = {"Cidades": chaves, "População": valores2}
        
        df = pd.DataFrame(dados).set_index("Cidades")

        st.title("Cidades com maior população")

        st.bar_chart(df, color='#f0f0f0')



        st.divider()

        for x in Cidades:
            dic.append(x.to_dict())

        st.header('Somar população de cidades')

        list = []

        ninputs = st.number_input('Número de cidades', step=1, min_value=1)
        st.write('Numero de cidades ', ninputs)

        for i in range(ninputs):
            input_values = st.selectbox(f"Cidade {i+1}", dic)
            list.append(input_values) 
                
        if st.button("Adicionar", key="button_update"):
            df = pd.DataFrame(list)
            st.dataframe(df)
            st.write(f'População somada: ', View.somar_cidade(list))