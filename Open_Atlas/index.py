from Template.loginUI import *
from Template.abrircontaUI import *
from Template.ManterUsuarioUI import *
from Template.ManterCidadeUI import *
from Template.ManterEstadoUI import *
from Template.ManterPaisUI import *
from Template.VisualizarCidadesUI import *
from Template.VisualizarEstadosUI import *
from Template.VisualizarPaisesUI import *
from Template.EditarPerfilUI import *
from views import *

import streamlit as st
import os

root = os.getcwd()

class IndexUI:
    def menu_visitante():    
        st.sidebar.image(
            f'{root}\Open_Atlas\Open_Atlas.svg', width=110
        )
        st.sidebar.markdown(
        '''
        <style>
            div[data-testid="stFullScreenFrame"]{
                display: flex;
                justify-content: center;
            }
        ''',
                unsafe_allow_html=True,
        )
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
               
    def menu_admin():  
        st.sidebar.image(
            f'{root}\Open_Atlas\Open_Atlas.svg', width=110
        )
        st.sidebar.markdown(
        '''
        <style>
            div[data-testid="stFullScreenFrame"]{
                display: flex;
                justify-content: center;
            }
        ''',
                unsafe_allow_html=True,
        )   
        st.sidebar.write("Bem-vindo(a), " + st.session_state["nome"])      
        op = st.sidebar.selectbox("Menu", ["Cadastro de Usuario", "Cadastro de Cidades", "Cadastro de Estados", "Cadastro de Paises", "Editar Perfil"])
        if op == "Cadastro de Usuario": ManterUsuarioUI.main()
        if op == "Cadastro de Cidades": ManterCidadeUI.main()
        if op == "Cadastro de Estados": ManterEstadoUI.main()
        if op == "Cadastro de Paises": ManterPaisUI.main()
        if op == "Editar Perfil": EditarPerfilUI.main()

    def menu_Usuario():
        st.sidebar.image(
            f'{root}\Open_Atlas\Open_Atlas.svg', width=110
        )
        st.sidebar.markdown(
        '''
        <style>
            div[data-testid="stFullScreenFrame"]{
                display: flex;
                justify-content: center;
            }
        ''',
                unsafe_allow_html=True,
        )
        st.sidebar.write("Bem-vindo(a), " + st.session_state["nome"])
        op = st.sidebar.selectbox("Menu", ["Visualizar Cidades", "Visualizar Estados", "Visualizar Paises", "Editar Perfil"])
        if op == "Visualizar Cidades": VisualizarCidadesUI.main()
        if op == "Visualizar Estados": VisualizarEstadosUI.main()
        if op == "Visualizar Paises": VisualizarPaisesUI.main()
        if op == "Editar Perfil": EditarPerfilUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["id"]
            del st.session_state["nome"]
            st.rerun()
    
    def sidebar():
        if "id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["nome"] == "admin"
            # mensagen de bem-vindo
            # menu do usuário
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_Usuario()
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
    
    def main():
        # verifica a existe o usuário admin
        View.usuario_admin()
        # monta o sidebar
        IndexUI.sidebar()
       
IndexUI.main()