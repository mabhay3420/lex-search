from collections import defaultdict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from search import search_similar
import json


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search/lex")
async def search_lex(q: str = None):
    if q is None:
        return {
            "data": {"error": {"message": "Please enter a search query."}},
        }
    
    context = await search_similar(q)
    response = {
        "success": "true",
        "data": {
            "query": q,
            "result": [
                {
                    "chunkInfo": episode["data"],
                    "episodeInfo": episode["info"],
                }
                for episode in context
            ],
        },
    }

    return response


if __name__ == "__main__":
    app.run(debug=True)