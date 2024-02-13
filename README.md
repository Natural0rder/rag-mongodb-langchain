# Prerequisites

- A [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) Cluster
- An OpenAI [API Key](https://openai.com/blog/openai-api)
- Python

Run the following commands to create your app based on rag-mongo template:

```
pip install langchain-cli
pip install openai
langchain app new <my-app-name> --package rag-mongo
```

```
export OPENAI_API_KEY=<my-openai-api-key>
export MONGO_URI=<my-mongodb-cs>
```

# Update app/server.py

Add the route to your app:

```
from rag_mongo import chain as rag_mongo_chain
add_routes(app, rag_mongo_chain, path="/rag-mongo")
```

# Update rag-mongo/ingest.py parameters

<img width="1158" alt="image" src="https://github.com/Natural0rder/rag-mongodb-langchain/assets/102281652/8277f250-034e-4db3-bddd-2cbeb486e104">

```
DB_NAME = "database-name"
COLLECTION_NAME = "collection-name"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector-index-name"
EMBEDDING_FIELD_NAME = "embedding"
# PDF file to split location
FILE_URI = "https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4HkJP" 
CHUNK_SIZE = 500
CHUNK_OVERLAP = 0
```

# Udpate rag-mongo/chain.py paramaters

<img width="1141" alt="image" src="https://github.com/Natural0rder/rag-mongodb-langchain/assets/102281652/e6cd759d-da4e-4c13-99e2-a6abd4c89a6b">

```
DB_NAME = "database-name"
COLLECTION_NAME = "collection-name"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector-index-name"
SEARCH_K_VALUE = 100
POST_FILTER_PIPELINE_LIMIT = 1
OPENAI_MODEL_NAME = "gpt-3.5-turbo-16k-0613"
```

# Run ingest.py to create documents

```
python3 ingest.py
```

# Create the Atlas Vector Search index

```
{
  "fields": [{
    "path": "embedding",
    "numDimensions": 1536,
    "similarity": "cosine",
    "type": "vector"
  }]
}
```

# Serve the app

Run LangServe at /app level

```
langchain serve
```

<img width="696" alt="image" src="https://github.com/Natural0rder/rag-mongodb-langchain/assets/102281652/dc7a9c04-a3cd-4c7e-8b44-7a8ffa919339">

# Browse the app

```
http://localhost:8000/rag-mongo/playground/
```

<img width="644" alt="image" src="https://github.com/Natural0rder/rag-mongodb-langchain/assets/102281652/4887cf14-96d6-4a27-a530-7e5d8e4ff3f7">



