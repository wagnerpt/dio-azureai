import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")  
    SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")
    ENDPOINT = os.getenv("ENDPOINT")