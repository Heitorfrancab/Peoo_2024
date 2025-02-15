import streamlit as st
import pandas as pd
from views import View
import time

class ManterUsuarioUI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Cadastro de Usuarios")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterUsuarioUI.listar()
        with tab2: ManterUsuarioUI.inserir()
        with tab3: ManterUsuarioUI.atualizar()
        with tab4: ManterUsuarioUI.excluir()

    def listar():
        Usuarios = View.usuario_listar()
        if len(Usuarios) == 0: 
            st.write("Nenhum Usuario cadastrado")
        else:    
            #for obj in Usuarios: st.write(obj)
            dic = []
            for obj in Usuarios: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do Usuario", placeholder = st.session_state["placeholder"])
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            if nome == "":
                st.session_state["placeholder"] = "O campo não pode estar vazio!"
                st.error("Informe o nome")
                time.sleep(2)
                st.rerun()
            else:
                View.Usuario_inserir(nome, email, fone, senha)
                st.success("Usuario inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        Usuarios = View.usuario_listar()
        if len(Usuarios) == 0: 
            st.write("Nenhum Usuario cadastrado")
        else:
            op = st.selectbox("Atualização de Usuario", Usuarios)
            nome = st.text_input("Informe o novo nome do Usuario", op.nome)
            email = st.text_input("Informe o novo e-mail", op.email)
            fone = st.text_input("Informe o novo fone", op.fone)
            senha = st.text_input("Informe a nova senha", op.senha, type="password")
            if st.button("Atualizar"):
                View.Usuario_atualizar(op.id, nome, email, fone, senha)
                st.success("Usuario atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Usuarios = View.Usuario_listar()
        if len(Usuarios) == 0: 
            st.write("Nenhum Usuario cadastrado")
        else:
            op = st.selectbox("Exclusão de Usuario", Usuarios)
            if st.button("Excluir"):
                View.Usuario_excluir(op.id)
                st.success("Usuario excluído com sucesso")
                time.sleep(2)
                st.rerun()