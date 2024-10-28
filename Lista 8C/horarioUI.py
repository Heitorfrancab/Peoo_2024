from horario import *
import streamlit as st
import pandas as pd

class HorarioUI:
    @staticmethod
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            df = pd.DataFrame(Horarios.listar())
            st.dataframe(df)
        with tab2:
            de = st.text_input("Informe a descrição: ")
            da = st.text_input("Informe a data (dd/mm/aaaa hh:mm): ")
            c = True
            idc = st.text_input("Informe o identificador do cliente: ")
            ids = st.text_input("Informe o identificador do serviço: ")
            if st.button("Inserir"):
                h = Horario(0, de, da, c, idc, ids)
                Horarios.inserir(h)
        with tab3:
            y = st.selectbox("Atualização de horários", Horarios.listar())
            de = st.text_input("Informe a nova descrição: ")
            da = st.text_input("Informe a nova data (dd/mm/aaaa): ")
            c = True
            idc = st.text_input("Informe o novo identificador do cliente: ")
            ids = st.text_input("Informe o novo identificador do serviço: ")
            if st.button("Atualizar horário"):
                h = Horario(y.id, de, da, c, idc, ids)
                Horarios.atualizar(h)
        with tab4:
            y = st.selectbox("Exclusão de Horarios", Horarios.listar())
            if st.button("Exluir horário"):
                x = Horario(y.id, "", "", "", "", "")
                Horarios.excluir(x)

HorarioUI.main()