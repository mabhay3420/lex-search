import numpy as np
from embed import generate_embeddings
from model_loader import model, tokenizer, provider
from index_loader import index
from content_loader import transcripts
from utils import timer, get_video_info
import fire



@timer
async def search_similar(query, text_list = transcripts, index = index, model = model, tokenizer = tokenizer, provider=provider, top_k=5):
    query_embedding = await generate_embeddings([query], model, tokenizer, provider)
    # return
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for distance, index in zip(distances[0], indices[0]):
        video_info = get_video_info(text_list[index]["episodeNumber"].lstrip('0'),text_list[index]['transcript']['start'])
        results.append({"distance": distance, "data": text_list[index], "info" : video_info})

    return results


if __name__ == "__main__":
    # search_similar_tweets("Hello",text_list, index, model, tokenizer, provider, top_k=5)
    fire.Fire(search_similar)
