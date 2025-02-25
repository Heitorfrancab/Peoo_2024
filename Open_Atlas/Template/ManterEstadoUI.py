import streamlit as st
import pandas as pd
from views import View
import time

class ManterEstadoUI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Cadastro de Estados")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "População"])
        with tab1: ManterEstadoUI.listar()
        with tab2: ManterEstadoUI.inserir()
        with tab3: ManterEstadoUI.atualizar()
        with tab4: ManterEstadoUI.excluir()
        with tab5: ManterEstadoUI.populacao()

    def listar():
        Estados = View.estado_listar()

        text_search = st.text_input("Pesquisar estados", value="")
        
        if st.button('Pesquisar'):
            if text_search != "":
                text_search = View.estado_pesquisar(text_search)
                if len(text_search) > 0:
                    df2 = pd.DataFrame(text_search)
                    st.dataframe(df2)
                else:
                    st.error('Nenhuma correspondência encontrada.')
                    time.sleep(2)
                    st.rerun()

        st.divider()

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
    
    def populacao():
        Estados = View.estado_listar()

        dic = []
        for obj in Estados:
            dic.append(obj.to_dict())   

        lista_estados = {}
        
        for x in Estados:
            n = x.get_nome()
            p = int(x.get_populacao())
            lista_estados[n] = p
        
        ordenada = dict(sorted(lista_estados.items(), key=lambda item: item[1], reverse=False))

        chaves = ordenada.keys()
        valores = ordenada.values()
        valores2 = sorted(valores)

        dados = {"Estados": chaves, "População": valores2}
        
        df = pd.DataFrame(dados).set_index("Estados")

        st.title("Estados com maior população")

        st.bar_chart(df, color='#f0f0f0')

        for x in Estados:
            dic.append(x.to_dict())


        st.divider()


        st.header('Somar população em um estado')

        op = st.selectbox("Somar populações do Estado", dic)
        id = op["ID"]
        
        if st.button('Somar'):
            st.write(View.somar_estado(id, []))

        st.divider()
    
        st.header('Somar população de estados')

        list = []

        ninputs = st.number_input('Número de estados', step=1, min_value=1)
        st.write('Numero de estados ', ninputs)

        for i in range(ninputs):
            input_values = st.selectbox(f"Estado {i+1}", dic)
            list.append(input_values) 
                
        if st.button("Adicionar", key="button_update"):
            df = pd.DataFrame(list)
            st.dataframe(df)
            st.write(f'População somada: ', View.somar_estado('', list))