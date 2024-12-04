import streamlit as st
from views import View
import time

class dadosUI:
    def main():
        st.header("Alterar Dados")
        clientes = st.session_state["clienteid"]

        if clientes == 1:
            dadosUI.atualizaradmin()
        else:
            dadosUI.atualizarcliente()

    def atualizarcliente():
        clientes = st.session_state["clienteid"]
        op = View.cliente_listar_id(clientes)

        nome = st.text_input("Informe o novo nome do cliente", op.nome)
        email = st.text_input("Informe o novo e-mail", op.email)
        fone = st.text_input("Informe o novo fone", op.fone)
        senha = st.text_input("Informe a nova senha", op.senha, type="password")
        perfil = View.perfil_listar()
        if st.button("Atualizar"):
            View.cliente_atualizar(op.id, nome, email, fone, senha, perfil.id)
            st.success("Dados atualizados com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizaradmin():
        op = View.cliente_listar_id(1)

        senha = st.text_input("Informe a nova senha", op.senha, type="password")

        if st.button("Atualizar"):
            View.cliente_atualizar(op.id, "admin", "admin", 1234, senha, 0)
            st.success("Dados atualizados com sucesso")
            time.sleep(2)
            st.rerun()