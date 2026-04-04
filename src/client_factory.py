import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient, DocumentModelAdministrationClient

class AzureClientFactory:
    def __init__(self):
        self.endpoint = os.getenv("DOC_INTELLIGENCE_ENDPOINT")
        self.key = os.getenv("DOC_INTELLIGENCE_KEY")
        if not self.endpoint or not self.key:
            raise ValueError("Missing Azure credentials")

    def get_analysis_client(self):
        return DocumentAnalysisClient(self.endpoint, AzureKeyCredential(self.key))

    def get_admin_client(self):
        return DocumentModelAdministrationClient(self.endpoint, AzureKeyCredential(self.key))
