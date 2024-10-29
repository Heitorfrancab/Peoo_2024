from cliente import *
import streamlit as st
import pandas as pd

class AutoCadastroUI:
    @staticmethod
    def main():
        st.header("Autocadastro de cliente")

        nome = st.text_input("Informe o seu nome")
        email = st.text_input("Informe o seu email")
        fone = st.text_input("Informe o seu fone")
        senha = st.text_input("Informe a sua senha")
        if st.button("Cadastrar"):
            x = Cliente(0, nome, email, fone, senha)
            Clientes.inserir(x)

AutoCadastroUI.main()