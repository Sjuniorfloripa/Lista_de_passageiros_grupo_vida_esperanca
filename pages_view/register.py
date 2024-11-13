import streamlit as st
import os
import pandas as pd
from utils import crud

def show_register_page():
    st.title("Registro de Pessoas")

    nome = st.text_input("Nome Completo")
    cpf = st.text_input("CPF")
    rg = st.text_input("RG")

    if st.button("Salvar"):
        if nome and (cpf or rg):
            
            cpf = crud.formatar_cpf(cpf) if cpf else ""
            crud.salvar_dados(nome, cpf, rg)
            st.success("Dados salvos com sucesso!")
        else:
            st.error("Por favor, preencha o Nome e pelo menos um entre CPF ou RG.")

    st.subheader("Integrantes Registrados")
    
    if os.path.exists("dados_pessoas.csv"):
        df = pd.read_csv("dados_pessoas.csv")
        if not df.empty:
            st.dataframe(df)
        else:
            st.write("Não foram encontrados registros no momento.")
    else:
        st.write("Não foram encontrados registros no momento.")
