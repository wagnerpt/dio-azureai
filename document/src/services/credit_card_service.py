from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analyze_document(card_url):
    # Create a Document Intelligence client
    credential = AzureKeyCredential(Config.SUBSCRIPTION_KEY)
    document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

    # Analyze the document
    request = AnalyzeDocumentRequest(url_source=card_url)  #model_id="prebuilt-creditCard")
    document_info = document_client.begin_analyze_document(
        "prebuilt-creditCard", request)

    return document_info.result()

def analyze_credit_card(card_url):   
    result = analyze_document(card_url)
    
    for document in result.documents:
        fields = document.get("fields", {})
        
        return {
            "card_name": fields.get("CardHolderName", {}).get("content"),
            "card_number": fields.get("CardNumber", {}).get("content"),
            "expire_date": fields.get("ExpirationDate", {}).get("content"),
            "card_cvv": fields.get("CardVerificationValue", {}).get("content"),
            "bank_name": fields.get("IssuingBank", {}).get("content")
        }