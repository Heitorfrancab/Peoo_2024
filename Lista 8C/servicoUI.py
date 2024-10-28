from servico import *
import streamlit as st
import pandas as pd

class ServicoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            df = pd.DataFrame(Servicos.listar())
            st.dataframe(df)
        with tab2:
            de = st.text_input("Informe a descrição do serviço: ")
            v = True
            d = st.text_input("Informe a duração: ")
            if st.button("Inserir serviço"):
                s = Servico(0, de, v, d)
                Servicos.inserir(s)
        with tab3:
            y = st.selectbox("Atualização de Serviços", Servicos.listar())
            de = st.text_input("Informe a nova descrição do serviço: ")
            v = True
            d = st.text_input("Informe a nova duração: ")
            if st.button("Atualizar serviço"):
                h = Servico(y.id, de, v, d)
                Servicos.atualizar(h)
        with tab4:
            y = st.selectbox("Exclusão de Serviços", Servicos.listar())
            if st.button("Exluir serviço"):
                x = Servico(y.id, "", "", "")
                Servicos.excluir(x)

ServicoUI.main()