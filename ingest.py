import os

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import MongoDBAtlasVectorSearch
from pymongo import MongoClient

MONGO_URI = os.environ["MONGO_URI"]

# Note that if you change this, you also need to change it in `rag_mongo/chain.py`
DB_NAME = "database-name"
COLLECTION_NAME = "collection-name"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector-index-name"
EMBEDDING_FIELD_NAME = "embedding"
# PDF file to split location
FILE_URI = "https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4HkJP" 
CHUNK_SIZE = 500
CHUNK_OVERLAP = 0

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
MONGODB_COLLECTION = db[COLLECTION_NAME]

if __name__ == "__main__":
    # Load docs
    loader = PyPDFLoader(FILE_URI)
    data = loader.load()

    # Split docs
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    docs = text_splitter.split_documents(data)

    # Insert the documents in MongoDB Atlas Vector Search
    _ = MongoDBAtlasVectorSearch.from_documents(
        documents=docs,
        embedding=OpenAIEmbeddings(disallowed_special=()),
        collection=MONGODB_COLLECTION,
        index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    )
