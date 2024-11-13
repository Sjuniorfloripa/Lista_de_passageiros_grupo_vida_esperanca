import streamlit as st

def show_welcome_page():
    st.title("Bem-vindo ao Aplicativo Grupo Vida e Esperança")
    st.write(
        """
        Este aplicativo foi desenvolvido para auxiliar no registro dos integrantes do grupo
        "Vida e Esperança". Com ele, você poderá:
        
        - Visualizar os registros de todos os integrantes do grupo.
        - Gerar uma lista com os nomes e CPFs de cada integrante.
        - Enviar automaticamente o PDF da lista para o WhatsApp do coordenador do grupo.

        Aproveite a facilidade e organização que o aplicativo oferece!
        """
    )
