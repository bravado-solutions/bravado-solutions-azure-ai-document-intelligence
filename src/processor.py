class DocumentProcessor:
    def __init__(self, client):
        self.client = client

    def run_analysis(self, model_id, url):
        try:
            poller = self.client.begin_analyze_document_from_url(model_id, url)
            result = poller.result()

            output = []
            for doc in result.documents:
                fields = {k: {"value": v.value or v.content, "conf": v.confidence}
                          for k, v in doc.fields.items()}
                output.append({"type": doc.doc_type, "data": fields})
            return output
        except Exception as e:
            raise Exception(f"Analysis failed: {str(e)}")
