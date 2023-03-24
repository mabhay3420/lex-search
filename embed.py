import torch
from embed_openai import embed_openai
from embed_local import embed_local
from utils import timer

@timer
def generate_embeddings(text_list, model, tokenizer, provider = None):

    if provider == "openai":
        return embed_openai(text_list)
    else:
        return embed_local(text_list, model, tokenizer)