import streamlit as st
import pandas as pd
from views import View
import time

class ManterPaisUI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Cadastro de Países")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterPaisUI.listar()
        with tab2: ManterPaisUI.inserir()
        with tab3: ManterPaisUI.atualizar()
        with tab4: ManterPaisUI.excluir()

    def listar():
        Paises = View.pais_listar()
        if len(Paises) == 0: 
            st.write("Nenhum país cadastrado")
        else:    
            dic = []
            for obj in Paises: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do país", placeholder = st.session_state["placeholder"])
        abrev = st.text_input("Informe a abreviação do país")
        nac = st.text_input("Informe a nacionalidade do país")
        moeda = st.text_input("Informe a moeda do país")
        populacao = st.text_input("Informe a população do país")
        capital = st.text_input("Informe o ID da capital")
        cod = st.text_input("Informe o código de internet do país")

        if st.button("Inserir"):
            if nome == "":
                st.session_state["placeholder"] = "O campo não pode estar vazio!"
                st.error("Informe o nome")
                time.sleep(2)
                st.rerun()
            else:
                View.pais_inserir(nome, abrev, nac, moeda, populacao, capital, cod)
                st.success("País inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        Paises = View.pais_listar()
        if len(Paises) == 0: 
            st.write("Nenhum país cadastrado")
        else:
            op = st.selectbox("Atualização de País", Paises)
            nome = st.text_input("Informe o novo nome do País", op.get_nome())
            abrev = st.text_input("Informe a nova abreviação do País", op.get_abrev())
            nac = st.text_input("Informe a nova nacionlidade do País", op.get_nac())
            moeda = st.text_input("Informe a nova moeda do País", op.get_moeda())
            populacao = st.text_input("Informe a nova população do País", op.get_populacao())
            capital = st.text_input("Informe o id da nova capital do País", op.get_capitalid())
            cod = st.text_input("Informe o novo código de internet do País", op.get_cod())

            if st.button("Atualizar"):
                View.pais_atualizar(op.id, nome, abrev, nac, moeda, populacao, capital, cod)
                st.success("Pais atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Paises = View.pais_listar()
        if len(Paises) == 0: 
            st.write("Nenhum país cadastrado")
        else:
            op = st.selectbox("Exclusão de Pais", Paises)
            if st.button("Excluir"):
                View.Pais_excluir(op.id)
                st.success("Pais excluído com sucesso")
                time.sleep(2)
                st.rerun()