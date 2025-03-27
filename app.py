import streamlit as st
import pandas as pd
import numpy as np


st.title("Visão Interativa com Streamlit")

st.header("Dados")

# Menu Lateral
st.sidebar.header("Menu Lateral")
option1 = st.sidebar.checkbox("Opção 1")
option2 = st.sidebar.checkbox("Opção 2")
option3 = st.sidebar.checkbox("Opção 3")

if option1:
    st.write("Você Selecionou a Opção 1")
if option2:
    st.write("Você Selecionou a Opção 2")
if option3:
    st.write("Você Selecionou a Opção 3")

# Criando um dataframe de exemplo
df = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])

st.subheader("Tabela de Dados")
st.dataframe(df)

st.subheader("Gráfico de Linhas")
st.line_chart(df)

# Widgets
if st.button("Mostrar Mensagem"):
    st.write("Botão Clicado!")

option = st.selectbox("Escolha uma Coluna para Visualizar", df.columns)

st.write("Você Selecionou: ", option)
st.bar_chart(df[option])