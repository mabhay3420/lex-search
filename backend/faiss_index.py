
# from fetch_tweets import fetch_tweets
from embed import generate_embeddings
from model_loader import model, tokenizer,provider
import json
from transformers import AutoTokenizer, AutoModel
import faiss
from utils import timer
import numpy as np
from content_loader import  transcripts, lex_video_info
# model_name = "sentence-transformers/paraphrase-MiniLM-L6-v2"

# # provider = "openai"
# provider  = None

# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModel.from_pretrained(model_name)

@timer
def create_faiss_index(embeddings):
    embeddings_matrix = np.vstack(embeddings)

    dimension = embeddings_matrix.shape[1]
    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings_matrix)

    return index

@timer
def update_faiss_index(text_list,new_index_file_path):
    batch_size = 2048
    # Generate tweet embeddings
    tweet_embeddings =  []
    for i in range(0,len(text_list),batch_size):
        batch = text_list[i:i+batch_size]
        batch_embedding = generate_embeddings(batch, model, tokenizer, provider)
        tweet_embeddings.extend(batch_embedding)
    
    # Create a FAISS index
    index = create_faiss_index(tweet_embeddings)

    faiss.write_index(index, new_index_file_path)


@timer
def get_faiss_index(index_file):
    index = faiss.read_index(index_file)
    return index




if __name__ == "__main__":
    new_index_file_path = "index_file.index"
    raw_transcript_text_list = [transcript["transcript"]["content"] for transcript in transcripts]
    update_faiss_index(raw_transcript_text_list, new_index_file_path)