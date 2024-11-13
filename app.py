import streamlit as st
from pages_view import welcome_page, register, create_passenger_list


PAGES = {
    "Bem-vindo": welcome_page.show_welcome_page,
    "Registro de Pessoas": register.show_register_page,
    "Criar Lista de Passageiros": create_passenger_list.show_create_passenger_list,
}

st.sidebar.title("Navegação")
selecionar_pagina = st.sidebar.radio("Escolha uma página:", list(PAGES.keys()))

pagina = PAGES[selecionar_pagina]
pagina()
