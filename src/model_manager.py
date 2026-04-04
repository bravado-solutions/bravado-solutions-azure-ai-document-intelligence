from azure.core.exceptions import HttpResponseError

class ModelManager:
    def __init__(self, client):
        self.client = client

    def build_custom_model(self, model_id, sas_url, desc):
        try:
            poller = self.client.begin_build_document_model(
                model_id=model_id,
                build_mode="neural",
                blob_container_url=sas_url,
                description=desc
            )
            return poller.result()
        except HttpResponseError as e:
            print(e)
            return None
