from cliente import *
import streamlit as st
import pandas as pd

class ClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            df = pd.DataFrame(Clientes.listar())
            st.dataframe(df)
        with tab2:
            nome = st.text_input("Informe o nome")
            email = st.text_input("Informe o email")
            fone = st.text_input("Informe o fone")
            if st.button("Inserir cliente"):
                x = Cliente(0, nome, email, fone)
                Clientes.inserir(x)
        with tab3:
            y = st.selectbox("Atualização de clientes", Clientes.listar())
            nome = st.text_input("Informe o novo nome")
            email = st.text_input("Informe o novo email")
            fone = st.text_input("Informe o novo fone")
            if st.button("Atualizar cliente"):
                x = Cliente(y.id, nome, email, fone)
                Clientes.atualizar(x)
        with tab4:
            y = st.selectbox("Exclusão de clientes", Clientes.listar())
            if st.button("Exluir cliente"):
                x = Cliente(y.id, "", "", "")
                Clientes.excluir(x)

ClienteUI.main()