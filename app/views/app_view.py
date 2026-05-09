import streamlit as st
import os
import requests



st.set_page_config(page_title='bibiotleca de livros')


API_URL = os.getenv('APi_URL')


st.title('gestor de livros')

with st.sidebar:
    st.header('novo livro')
    titulo = st.text_input('digite o livro: ')
    autor = st.text_input('autor: ')
    if st.button('cadastrar'):
        res = requests.post(API_URL, json={'titulo': titulo, 'autor': autor})
        if res.status_code == 200:
            st.success('livro salvo')
        else:
            st.error('ocorrwu um erro')

st.subheader('livro disponiveis')
if st.button('livros disponivies'):
    try:
        livros = requests.get(API_URL).json()
        for i in livros:
            st.info(f'{i['titulo']} : {i['autor']}')
    except:
        st.error('não foi possivel conectar a api - verifique... o servidor')
