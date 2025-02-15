import streamlit as st
import pandas as pd
from views import View
import time

class ManterCidadeUI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Cadastro de Cidades")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCidadeUI.listar()
        with tab2: ManterCidadeUI.inserir()
        with tab3: ManterCidadeUI.atualizar()
        with tab4: ManterCidadeUI.excluir()

    def listar():
        Cidades = View.cidade_listar()
        if len(Cidades) == 0: 
            st.write("Nenhuma cidade cadastrada")
        else:    
            dic = []
            for obj in Cidades: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        estados = View.estado_listar()

        nome = st.text_input("Informe o nome do cidade", placeholder = st.session_state["placeholder"])
        nat = st.text_input("Informe a naturalidade da cidade")
        populacao = st.text_input("Informe a população da cidade")
        estado = st.selectbox("Selecione o estado", estados, index = None)

        if st.button("Inserir"):
            if estado != None:
                idestado = estado.get_id()
            if nome == "":
                st.session_state["placeholder"] = "O campo não pode estar vazio!"
                st.error("Informe o nome")
                time.sleep(2)
                st.rerun()
            else:
                View.cidade_inserir(nome, nat, populacao, idestado)
                st.success("Cidade inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        Cidades = View.cidade_listar()
        if len(Cidades) == 0: 
            st.write("Nenhuma cidade cadastrado")
        else:
            estados = View.estado_listar()

            op = st.selectbox("Atualização de cidade", Cidades)
            nome = st.text_input("Informe o novo nome da Cidade", op.get_nome())
            nat = st.text_input("Informe a nova naturalidade da cidade", op.get_nat())
            populacao = st.text_input("Informe a nova população", op.get_populacao())
            estado = st.selectbox("Selecione o novo estado", estados, index = None)

            idestado = estado.get_id()
            if st.button("Atualizar"):
                View.cidade_atualizar(op.id, nome, nat, populacao, idestado)
                st.success("Cidade atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Cidades = View.cidade_listar()
        if len(Cidades) == 0: 
            st.write("Nenhuma cidade cadastrada")
        else:
            op = st.selectbox("Exclusão de cidade", Cidades)
            if st.button("Excluir"):
                View.cidade_excluir(op.id)
                st.success("Cidade excluída com sucesso")
                time.sleep(2)
                st.rerun()