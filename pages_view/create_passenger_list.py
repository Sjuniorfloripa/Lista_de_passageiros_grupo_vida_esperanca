import streamlit as st
import pandas as pd
from utils import pdf_generation
import os
from pathlib import Path


def carregar_dados():
    if os.path.exists("dados_pessoas.csv"):
        return pd.read_csv("dados_pessoas.csv")
    else:
        return pd.DataFrame(columns=["Nome Completo", "CPF", "RG"])

def salvar_pdf_em_downloads(pdf_path):
    downloads_path = str(Path.home() / "Downloads")
    destino = os.path.join(downloads_path, os.path.basename(pdf_path))
    os.replace(pdf_path, destino)
    return destino

def show_create_passenger_list():
    st.title("Criar Lista de Passageiros")
    
    if "passageiros_selecionados" not in st.session_state:
        st.session_state.passageiros_selecionados = []

    df = carregar_dados()
    if df.empty:
        st.write("Não há registros para listar passageiros.")
        return

    busca_nome = st.text_input("Buscar pelo nome")

    if busca_nome:
        df_filtrado = df[df["Nome Completo"].str.contains(busca_nome, case=False)]
    else:
        df_filtrado = df

    df_filtrado = df_filtrado[~df_filtrado["Nome Completo"].isin(st.session_state["passageiros_selecionados"])]

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Pessoas Registradas")
            if df_filtrado.empty:
                st.warning("Sem registros encontrados.")
            else:
                for _, row in df_filtrado.iterrows():
                    nome = row['Nome Completo']
                    if st.button(f"Incluir {nome}", key=f"incluir_{nome}"):
                        st.session_state["passageiros_selecionados"].append(nome)
                        st.rerun()

    with col2:
        with st.container(border=True):
            st.subheader("Passageiros Selecionados")
            if st.session_state.passageiros_selecionados:
                for nome in st.session_state.passageiros_selecionados:
                    if st.button(f"Remover {nome}", key=f"remover_{nome}"):
                        st.session_state["passageiros_selecionados"].remove(nome)
                        st.rerun()
            else:
                st.write("Ninguém ainda foi selecionado.")

    if st.button("Gerar PDF"):
        pdf_path = pdf_generation.gerar_pdf(st.session_state["passageiros_selecionados"])
        destino = salvar_pdf_em_downloads(pdf_path)
        st.success(f"PDF gerado com sucesso e salvo em: {destino}")
