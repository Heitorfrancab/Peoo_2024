import streamlit as st
from views import View
import time

class EditarPerfilUI:
    def main():
        id = st.session_state["id"]
        

        if st.session_state["nome"] == 'admin':
            email = View.usuario_listar_id(id).get_email()
            nome = st.session_state["nome"]
            senha = st.text_input("Informe a nova senha para o administrador", type="password")
            if st.button("Atualizar Administrador"):
                if senha != "":
                    View.usuario_atualizar(id, email, nome, senha)
                    st.success("Administrador atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                else:
                    senha = View.usuario_listar_id(id).get_senha()
                    View.usuario_atualizar(id, email, nome, senha)
                    st.success("Administrador atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
        else:
            nome = st.text_input("Informe o seu novo nome", st.session_state["nome"])
            email = st.text_input("Informe o novo e-mail", View.usuario_listar_id(id).get_email())
            senha = st.text_input("Informe a nova senha", type="password")
            if st.button("Atualizar Conta"):
                if senha != "":
                    View.usuario_atualizar(id, email, nome, senha)
                    st.success("Usuario atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                else:
                    senha = View.usuario_listar_id(id).get_senha()
                    View.usuario_atualizar(id, email, nome, senha)
                    st.success("Usuario atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()