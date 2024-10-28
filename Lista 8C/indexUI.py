from clienteUI import *
from horarioUI import *
from servicoUI import *
import streamlit as st

class IndexUI:
    @staticmethod
    def main():
        with st.sidebar:
            escolha = st.selectbox("Menu", ["Cadastro de clientes", "Cadastro de horários", "Cadastro de serviços"])

        if escolha == "Cadastro de clientes":
            ClienteUI.main()
        elif escolha == "Cadastro de horários":
            HorarioUI.main()
        elif escolha == "Cadastro de serviços":
            ServicoUI.main()

IndexUI.main()