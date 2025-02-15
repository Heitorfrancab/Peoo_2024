import streamlit as st
from views import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    def inserir():
        email = st.text_input("Informe o e-mail")
        nome = st.text_input("Informe o nome")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            View.usuario_inserir(email, nome, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()