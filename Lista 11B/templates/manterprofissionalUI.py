import streamlit as st
import pandas as pd
from views import View
import time

class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:    
            dic = []
            for obj in profissionais: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do profissional")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            View.profissional_inserir(nome, especialidade, conselho, email, senha)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de profissional", profissionais)
            nome = st.text_input("Informe o novo nome do profissional", op.nome)
            especialidade = st.text_input("Informe a nova especialidade", op.especialidade)
            conselho = st.text_input("Informe o novo conselho", str(op.conselho))
            email = st.text_input("Informe o e-mail")
            senha = st.text_input("Informe a senha", type="password")
            if st.button("Atualizar"):
                View.profissional_atualizar(op.id, nome, especialidade, conselho, email, senha)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de profissional", profissionais)
            if st.button("Excluir"):
                View.profissional_excluir(op.id)
                st.success("Profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()