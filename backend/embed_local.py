import torch
from utils import timer
import numpy as np


@timer
async def embed_local(text_list, model, tokenizer) :
    text_embeddings = []

    # Preprocess and create embeddings for each tweet
    for text in text_list:
        inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)

        with torch.no_grad():
            outputs = model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1).numpy()

        text_embeddings.append(embeddings.squeeze(0))
    
    text_embeddings = np.array(text_embeddings)

    return text_embeddings
