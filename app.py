import streamlit as st
import qrcode as qr
import os

st.title('Gerador de qrcode')

link = st.text_input('Digite o link: ')

botao = st.button('Gerar qrcode')

if not link:
    st.warning('Digite o link, por favor!')
else:
    if botao:
        img = qr.make(link)
        file_path = 'qr_legal.png'
        img.save(file_path)
        st.image(file_path, width=300)

        with open(file_path, 'rb') as file:
            down = st.download_button(label='Baixar qr code',
                            data=file,
                            file_name='qr_code legal.png',
                            mime='image/png')
            
            if down:
                os.remove(file_path)
                st.info('Baixado e excluído do servidor')

        






        
        