import streamlit as st
from EquacaoII import *

class EquacaoUI():
    def main():
        st.header("Equação e gráfico do segundo grau")
        a = st.text_input("a")
        b = st.text_input("b")
        c = st.text_input("c")
        if st.button("Calcular"):
            x = Equacao(a, b, c)
            st.write(x.__str__())

            chartdata = [(1, 3), (2, 5), (3, 7)]
           

            st.line_chart(
            chartdata,
            x="col1",
            y="col2"
            )