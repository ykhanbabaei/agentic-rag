from typing import Sequence

from langchain_classic.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from qdrant_client.models import Distance, VectorParams
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
import logging


logger = logging.getLogger(__name__)

class RagService:

    def __init__(self):
        if self.create_collection():
            self.vector_store = self.create_vector_store()
            self.load_chunk_store()
        else:
            self.vector_store = self.create_vector_store()


    def retrieve_documents(self, query: str) -> Sequence[Document]:
        docs = self.vector_store.similarity_search_with_score(query)
        seq_docs = [doc for doc,_ in docs]

        # reranker
        cross_encoder = HuggingFaceCrossEncoder(model_name="cross-encoder/ms-marco-MiniLM-L-6-v2")
        reranker = CrossEncoderReranker(model=cross_encoder, top_n=2)
        return reranker.compress_documents(documents=seq_docs, query=query)

    def load_chunk_store(self):
        logger.info("indexing data started")
        # load documents
        loader = PyPDFLoader("./sample_data/pdf/sample_company_policies_rag.pdf")
        docs = loader.load()

        # chunk documents
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
        chunks = splitter.split_documents(docs)

        # embed and store documents
        self.vector_store.add_documents(documents=chunks)
        logger.info("indexing data finished and stored in vector store")


    @staticmethod
    def create_vector_store():
        embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
        client = QdrantClient(path=os.getenv('QDRANT_STORAGE_PATH'))
        return QdrantVectorStore(
            client=client,
            collection_name=os.getenv('COLLECTION'),
            embedding=embedding,
        )

    @staticmethod
    def create_collection():
        client = QdrantClient(path=os.getenv('QDRANT_STORAGE_PATH'))
        if client.collection_exists(collection_name=os.getenv('COLLECTION')):
            return False
        embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
        vector_size = len(embedding.embed_query("sample text"))
        client.create_collection(collection_name=os.getenv('COLLECTION'), vectors_config = VectorParams(size=vector_size, distance=Distance.COSINE))
        logger.info("new collection created")
        return True


load_dotenv()
rag_service = RagService()