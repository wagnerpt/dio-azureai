# py -m pip install azure.storage.blob
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import streamlit as st
from utils.Config import Config

def upload_blob(file, filename):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=filename)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as e:
        st.write(f'Erro ao enviar o arquivo para o Blob de Armazenamento: {e}')
        return None