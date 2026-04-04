import os, pyodbc, logging

class DatabaseManager:
    def __init__(self):
        self.conn = os.getenv("SQL_CONNECTION_STRING")
        if not self.conn:
            raise ValueError("Missing DB connection")

    def save_extraction(self, doc_type, fields):
        try:
            with pyodbc.connect(self.conn) as conn:
                cur = conn.cursor()
                for k,v in fields.items():
                    cur.execute(
                        "INSERT INTO ExtractedDocuments VALUES (?, ?, ?, ?)",
                        doc_type, k, str(v['value']), v['conf']
                    )
                conn.commit()
        except Exception as e:
            logging.error(str(e))
            raise
