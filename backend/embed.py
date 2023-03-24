import torch
from embed_openai import embed_openai
from embed_local import embed_local
from utils import timer

@timer
async def generate_embeddings(text_list, model, tokenizer, provider = None):

    if provider == "openai":
        return await embed_openai(text_list)
    else:
        return await embed_local(text_list, model, tokenizer)