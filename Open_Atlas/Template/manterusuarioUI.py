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
            for obj in Usuarios: dic.append(obj.to_dict())
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do Usuario", placeholder = st.session_state["placeholder"])
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            if nome == "":
                st.session_state["placeholder"] = "O campo não pode estar vazio!"
                st.error("Informe o nome")
                time.sleep(2)
                st.rerun()
            else:
                View.usuario_inserir(email, nome, senha)
                st.success("Usuario inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        Usuarios = View.usuario_listar()
        dic = []
        for obj in Usuarios: 
            dic.append(obj.to_dict())
        if len(Usuarios) == 0: 
            st.write("Nenhum Usuario cadastrado")
        else:
            op = st.selectbox("Atualização de Usuario", dic)
            id = op['ID']
            nome = st.text_input("Informe o novo nome do Usuario", op['Nome'])
            email = st.text_input("Informe o novo e-mail", op['Email'])
            senha = st.text_input("Informe a nova senha", type="password")
            if st.button("Atualizar"):
                if senha != "":
                    View.usuario_atualizar(id, email, nome, senha)
                else:
                    senha = View.usuario_listar_id(id).get_senha()
                    View.usuario_atualizar(id, email, nome, senha)
                st.success("Usuario atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Usuarios = View.usuario_listar()
        dic = []
        for obj in Usuarios: 
            dic.append(obj.to_dict())
        if len(Usuarios) == 0: 
            st.write("Nenhum Usuario cadastrado")
        else:
            op = st.selectbox("Exclusão de Usuario", dic)
            if st.button("Excluir"):
                View.usuario_excluir(op['ID'])
                st.success("Usuario excluído com sucesso")
                time.sleep(2)
                st.rerun()