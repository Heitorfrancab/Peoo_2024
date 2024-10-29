from clienteUI import *
from horarioUI import *
from servicoUI import *
from autocadastroUI import *
import streamlit as st

class IndexUI:
    @staticmethod
    def main():
        with st.sidebar:
            escolha = st.selectbox("Menu", ["Cadastro de clientes", "Cadastro de horários", "Cadastro de serviços"])
            st.button("Criar conta", type="primary")
            
        if escolha == "Cadastro de clientes":
            ClienteUI.main()

        if escolha == "Cadastro de horários":
            HorarioUI.main()

        if escolha == "Cadastro de serviços":
            ServicoUI.main()

        if st.sidebar.button:
            AutoCadastroUI.main()

IndexUI.main()