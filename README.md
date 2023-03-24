# Lex Fridman Podcast search

Search for a phrase or question from all across Lex Fridman Podcast

## Setup
### 1. Backend setup
a.  Move to backend directory : `cd backend`

b.  Install dependencies in a new venv, checked with python3.8

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.tx
```

c. Fill in environment variables(Optional): `cp .env.example .env`

d. Run `python main.py`

e. Check if things are fine by running
```bash
curl -X GET "http://localhost:8000/search/lex?query=fastapi" -H "accept: application/json"
```

### 2. Frontend Setup:
a. Move to frontend directory: `cd frontend`
b. Install dependecies : `npm install`
c. Run : `npm start`
d. Go to [http://localhost:3000](http://localhost:3000)

### 3. (Optional) Discord bot:
a. Go to backend : `cd backend`

b. Fill DISCORD_BOT_TOKEN and DISCORD_CLIENT_ID in .env file `cp .env.example .env`

c. (Optional) To summarize using `chatgpt` Fill `OPENAI_API_KEY` with your api key and set `USE_CHAT_GPT` to some non empty value say `1`

d. activate venv `source venv/bin/activate`

e. Run bot:  `python bot.py`

The bot should have access to read and send messages in the server.


## Implementation Details
Thanks ChatGPT
1. Get transcript data from [Karpathy's Blog](link here)
2. Process transcript data. Sample after processing(from `merged_transcripts.json`)

```
[
    {
        "episodeNumber": "188",
        "chunk": 0,
        "transcript": {
            "start": "00:00.000",
            "end": "00:56.560",
            "content": "The following is a conversation with Vitalik Buterin, his second time on the podcast."
        }
    },

```
3. Get some information for each episode using `youtubesearchpython`. Sample(from `lex_video_info.json`)
```
{
    "366": {
        "title": "Shannon Curry: Johnny Depp & Amber Heard Trial, Marriage, Dating & Love | Lex Fridman Podcast #366",
        "link": "https://www.youtube.com/watch?v=qtOKrG_wK5A&list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4&index=1"
    },
```
4. Embed each of these chunks using `sentence-transformer` model(Can use any other model such as OpenAI's `ada-002`)
5. Store these embeddings in a `faiss` index
6. Upon recieving a query, embed it, perform similarity search on index, get the most relevant chunk and use the information in chunk and episode information to return the title and link to relevant timestamp.
