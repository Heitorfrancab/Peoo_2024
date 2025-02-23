import streamlit as st
import pandas as pd
from views import View
import time

class ManterEstadoUI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Cadastro de Estados")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterEstadoUI.listar()
        with tab2: ManterEstadoUI.inserir()
        with tab3: ManterEstadoUI.atualizar()
        with tab4: ManterEstadoUI.excluir()

    def listar():
        Estados = View.estado_listar()
        if len(Estados) == 0: 
            st.write("Nenhum estado cadastrado")
        else:    
            dic = []
            for obj in Estados: dic.append(obj.to_dict())
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        paises = View.pais_listar()
        dic = []
        for obj in paises:
            dic.append(obj.to_dict())

        nome = st.text_input("Informe o nome do estado", placeholder = st.session_state["placeholder"])
        abrev = st.text_input("Informe a abreviação do estado")
        nat = st.text_input("Informe a naturalidade do estado")
        populacao = st.text_input("Informe a população do estado")

        pais = st.selectbox("Selecione o país", dic)

        if st.button("Inserir"):
            if pais != None:
                idpais = pais['ID']
            if nome == "":
                st.session_state["placeholder"] = "O campo não pode estar vazio!"
                st.error("Informe o nome")
                time.sleep(2)
                st.rerun()
            else:
                View.estado_inserir(nome, abrev, nat, populacao, idpais)
                st.success("Estado inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        Estados = View.estado_listar()
        dic = []
        for obj in Estados:
            dic.append(obj.to_dict())

        if len(Estados) == 0: 
            st.write("Nenhum estado cadastrado")

        else:
            paises = View.pais_listar()
            dic_p = []
            for obj in paises:
                dic_p.append(obj.to_dict())

            op = st.selectbox("Atualização de Estado", dic)
            id = op['ID']
            nome = st.text_input("Informe o novo nome do Estado", op['Nome'])
            abrev = st.text_input("Informe a nova abreviação do Estado", op['Abreviação'])
            nat = st.text_input("Informe a nova naturalidade do Estado", op['Naturalidade'])
            populacao = st.text_input("Informe a nova população do estado", op['População'])

            opais = st.selectbox("Selecione o novo país", dic_p)
            idpais = opais['ID']

            if st.button("Atualizar"):
                View.estado_atualizar(id, nome, abrev, nat, populacao, idpais)
                st.success("Estado atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Estados = View.estado_listar()
        dic = []
        for obj in Estados:
            dic.append(obj.to_dict())
        if len(Estados) == 0:
            st.write("Nenhum estado cadastrado")
        else:
            op = st.selectbox("Exclusão de Estado", dic)
            if st.button("Excluir"):
                View.estado_excluir(op['ID'])
                st.success("Estado excluída com sucesso")
                time.sleep(2)
                st.rerun()