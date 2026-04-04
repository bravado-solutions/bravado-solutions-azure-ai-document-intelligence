import azure.functions as func
import logging, json
from src.client_factory import AzureClientFactory
from src.processor import DocumentProcessor
from src.database_manager import DatabaseManager

app = func.FunctionApp()

@app.queue_trigger(arg_name="msg", queue_name="doc-processing-queue",
                   connection="AzureWebJobsStorage")
def process_document_queue(msg: func.QueueMessage):
    logging.info("Processing document")

    try:
        body = json.loads(msg.get_body().decode())
        factory = AzureClientFactory()
        processor = DocumentProcessor(factory.get_analysis_client())
        db = DatabaseManager()

        results = processor.run_analysis(body["model_id"], body["url"])

        for res in results:
            db.save_extraction(res['type'], res['data'])

        logging.info("SUCCESS")

    except Exception as e:
        logging.error(f"FAILURE: {str(e)}")
        raise
