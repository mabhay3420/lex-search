import openai
from openai.embeddings_utils import get_embeddings 
from utils import timer
import numpy as np
from creds import OPENAI_API_KEY


openai.api_key = OPENAI_API_KEY
@timer
def embed_openai(text_list):
    embeddings = get_embeddings(text_list, engine="text-embedding-ada-002")
    return np.array(embeddings)
