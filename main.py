import requests
import streamlit as st


def buscar_letra(banda, musica):
    endpoint = f'https://api.lyrics.ovh/v1/{banda}/{musica}'
    response = requests.get(endpoint)
    letra = response.json()['lyrics'] if response.status_code == 200 else ''
    return letra

st.image('...')
st.title('Letras de músicas')
response = requests.get(endpoint)

banda = st.text_input('Digite o nome da banda/cantor: ', key='banda')
musica = st.text_input('Digite o nome da música: ', key='music')
pesquisar = st.button('Pesquisar')

if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success('Encontramos a letra da sua música!')
        st.text(letra)
    else:
        st.error('Infelizmente não foi possivel encontrar a letra dessa música!')
