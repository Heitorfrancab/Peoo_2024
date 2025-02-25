import streamlit as st
import pandas as pd
from views import View
import time

class ManterPaisUI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Cadastro de Países")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "População"])
        with tab1: ManterPaisUI.listar()
        with tab2: ManterPaisUI.inserir()
        with tab3: ManterPaisUI.atualizar()
        with tab4: ManterPaisUI.excluir()
        with tab5: ManterPaisUI.populacao()

    def listar():
        Paises = View.pais_listar()

        text_search = st.text_input("Pesquise países", value="")
        
        if st.button('Pesquisar'):
            if text_search != "":
                text_search = View.pais_pesquisar(text_search)
                if len(text_search) > 0:
                    df2 = pd.DataFrame(text_search)
                    st.dataframe(df2)
                else:
                    st.error('Nenhuma correspondência encontrada.')
                    time.sleep(2)
                    st.rerun()

        st.divider()

        if len(Paises) == 0: 
            st.write("Nenhum país cadastrado")
        else:    
            dic = []
            for obj in Paises: dic.append(obj.to_dict())
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
                st.write(nome + abrev + nac + moeda + populacao + capital + cod)
                View.pais_inserir(nome, abrev, nac, moeda, populacao, capital, cod)
                st.success("País inserido com sucesso")
                time.sleep(2)
                # st.rerun()

    def atualizar():
        Paises = View.pais_listar()
        if len(Paises) == 0: 
            st.write("Nenhum país cadastrado")
        else:
            dic = []
            for obj in Paises: dic.append(obj.to_dict())

            op = st.selectbox("Atualização de País", dic)
            id = op['ID']
            nome = st.text_input("Informe o novo nome do País", op['Nome'])
            abrev = st.text_input("Informe a nova abreviação do País", op['Abreviação'])
            nac = st.text_input("Informe a nova nacionlidade do País", op['Nacionalidade'])
            moeda = st.text_input("Informe a nova moeda do País", op['Moeda'])
            populacao = st.text_input("Informe a nova população do País", op['População'])
            capital = st.text_input("Informe o id da nova capital do País", op['ID da capital'])
            cod = st.text_input("Informe o novo código de internet do País", op['Código de internet'])

            if st.button("Atualizar"):
                View.pais_atualizar(id, nome, abrev, nac, moeda, populacao, capital, cod)
                st.success("Pais atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Paises = View.pais_listar()
        if len(Paises) == 0: 
            st.write("Nenhum país cadastrado")
        else:
            dic = []
            for obj in Paises: dic.append(obj.to_dict())
            op = st.selectbox("Exclusão de Pais", dic)
            if st.button("Excluir"):
                View.pais_excluir(op['ID'])
                st.success("Pais excluído com sucesso")
                time.sleep(2)
                st.rerun()
    def populacao():
        Paises = View.pais_listar()
        dic = []
        for obj in Paises:
            dic.append(obj.to_dict())  

        lista_paises = {}
        
        for x in Paises:
            n = x.get_nome()
            p = int(x.get_populacao())
            lista_paises[n] = p
        
        ordenada = dict(sorted(lista_paises.items(), key=lambda item: item[1], reverse=False))

        chaves = ordenada.keys()
        valores = ordenada.values()
        valores2 = sorted(valores)

        dados = {"Países": chaves, "População": valores2}
        
        df = pd.DataFrame(dados).set_index("Países")

        st.title("Países com maior população")

        st.bar_chart(df, color='#f0f0f0')

        st.divider()


        st.header('Somar população em um país')

        op = st.selectbox("Somar populações de um país", dic)
        id = op["ID"]
        
        if st.button('Somar'):
            st.write(View.somar_pais(id, []))

        st.divider()
    
        st.header('Somar população de países')

        list = []

        ninputs = st.number_input('Número de países', step=1, min_value=1)
        st.write('Numero de países ', ninputs)

        for i in range(ninputs):
            input_values = st.selectbox(f"País {i+1}", dic)
            list.append(input_values) 
                
        if st.button("Adicionar", key="button_update"):
            df = pd.DataFrame(list)
            st.dataframe(df)
            st.write(f'População somada: ', View.somar_pais('', list))