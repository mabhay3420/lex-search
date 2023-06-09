import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
DISCORD_CLIENT_ID = os.environ.get('DISCORD_CLIENT_ID')
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
USE_CHAT_GPT = os.environ.get('USE_CHAT_GPT')
