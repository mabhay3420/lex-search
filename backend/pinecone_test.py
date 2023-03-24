import pinecone
import numpy as np
from creds import PINECONE_API_KEY
from embed import generate_embeddings
from model_loader import model

# Initialize Pinecone client
pinecone.init(api_key=PINECONE_API_KEY)

# Initialize Sentence-BERT model

# Generate embeddings for some sentences
sentences = ["This is an example sentence.", "Another sentence."]
embeddings = generate_embeddings(sentences)

# Create Pinecone index
pinecone_index = pinecone.Index(index_name="sentence_embeddings", dimension=embeddings.shape[1])
pinecone_index.create_index()

# Upsert the embeddings as vectors
vectors = [(i, embeddings[i]) for i in range(len(sentences))]
pinecone_index.upsert(vectors)

# Query the index
query = ["Example sentence."]
query_embedding = model.encode(query)
results = pinecone_index.query(queries=[query_embedding], top_k=10)

# Print the results
for result in results[0]["matches"]:
    print(f"Sentence: {sentences[result['id']]} Score: {result['score']}")
