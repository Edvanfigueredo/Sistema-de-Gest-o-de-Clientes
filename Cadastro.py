import streamlit as st
import pandas as pd
from datetime import date

data_minima = date(1900, 1, 1)
data_maxima = date.today()

def gravar_cliente(nome, dt_nasc, tipo_cliente):
    if nome and data_minima <= dt_nasc <= data_maxima:
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{dt_nasc},{tipo_cliente}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de Clientes", 
    page_icon="👥",
      )

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente: ",
                     key="nome_cliente")
dt_nasc = st.date_input("Digite a data de nascimento do cliente: ", format="DD/MM/YYYY")
tipo_cliente = st.selectbox("Selecione o tipo de cliente: ",
                            options=["Pessoa Física", "Pessoa Jurídica"])

btn_cadastrar = st.button("Cadastrar Cliente",
                          on_click=gravar_cliente,
                          args=(nome, dt_nasc, tipo_cliente))

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Erro ao cadastrar cliente. Verifique os dados e tente novamente.",
                 icon="❌")
        