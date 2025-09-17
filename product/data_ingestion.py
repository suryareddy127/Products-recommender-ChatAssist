from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from product.data_converter import DataConverter
from product.config import config

class DataIngestion:
    def __init__(self):
        self.embedding = HuggingFaceEndpointEmbeddings(model=config.EMBEDDING_MODEL)
        
        self.vstore = AstraDBVectorStore(
            embedding=self.embedding,
            collection_name="productsdatabase",
            api_endpoint=config.ASTRA_DB_API_ENDPOINT,
            token=config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=config.ASTRA_DB_KEYSPACE
        )
        
    def ingest_data(self,load_existing:True):
        if load_existing==True:
            return self.vstore

        docs = DataConverter("data/Product_review.csv").convert_to_documents()
        
        self.vstore.add_documents(docs)
        return self.vstore


