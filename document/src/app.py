# py -m pip install streamlit, pandas
import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interfaces():
    st.title('Upload de arquivos DIO - Azure - Docs')
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        filename = uploaded_file.name
        #Enviar para o Blobo de Armazenamento
        blob_url = upload_blob(uploaded_file, filename)
        if blob_url:
            st.write('URL do arquivo:', blob_url)   
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write('Erro ao enviar o arquivo para o Blob de Armazenamento')
        
def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption='Imagem do cartão de crédito', use_container_width = True)
    st.write('Informações do cartão de crédito:')
    if credit_card_info and credit_card_info['card_name']:
        st.markdown(f'<h1 style="color: green;">Cartão Válido</h1>', unsafe_allow_html=True)
        st.write(f"Nome: {credit_card_info['card_name']}")
        st.write(f"Número: {credit_card_info['card_number']}")
        st.write(f"Validade: {credit_card_info['expire_date']}")
        st.write(f"CVV: {credit_card_info['card_cvv']}")
        st.write(f"Banco: {credit_card_info['bank_name']}")
    else:
        st.markdown(f'<h1 style="color: red;">Cartão Inválido</h1>', unsafe_allow_html=True)

if __name__ == '__main__':
    configure_interfaces()
    
    