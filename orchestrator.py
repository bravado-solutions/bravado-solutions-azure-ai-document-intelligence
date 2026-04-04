import os, json
from dotenv import load_dotenv
from azure.storage.queue import QueueClient
from src.client_factory import AzureClientFactory
from src.model_manager import ModelManager

load_dotenv()

factory = AzureClientFactory()

MODEL_ID = os.getenv("MODEL_ID")
SAS_URL = os.getenv("CONTAINER_SAS_URL")

if SAS_URL:
    ModelManager(factory.get_admin_client()).build_custom_model(
        MODEL_ID, SAS_URL, "Bravado Model"
    )

queue = QueueClient.from_connection_string(
    os.getenv("AZURE_STORAGE_CONNECTION_STRING"),
    "doc-processing-queue"
)

docs = ["https://example.com/doc1.pdf"]

for d in docs:
    queue.send_message(json.dumps({"url": d, "model_id": MODEL_ID}))
