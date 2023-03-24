from creds import OPENAI_API_KEY, USE_CHAT_GPT
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from utils import get_video_info

from search import search_similar

# Initialize the chat model
chat = ChatOpenAI(temperature=0)

# Create the SystemMessage template
system_message_template = SystemMessagePromptTemplate.from_template(
    "You are a SentientBot that answers questions, provide relevant summary, information etc. based on data from {source}."
)

# Create the HumanMessage template
human_message_template = HumanMessagePromptTemplate.from_template("Context: {context}.\n Message: {message}")

# Combine the templates into a ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages([system_message_template, human_message_template])

# Create an LLMChain with the chat model and chat prompt
chain = LLMChain(llm=chat, prompt=chat_prompt)

# Function to ask the chatbot for translations
def respond(message, context):
    return chain.run(source="Lex Fridman Podcast", message=message, context=context)

# Example usage
# print(translate("I love programming."))



# openai.api_key = OPENAI_API_KEY

async def generate_response(message):
    context = await search_similar(message)
    processed_context = "\n".join([f"{i}. {c['data']['transcript']['content']}" for i, c in enumerate(context)])
    print(processed_context)

    if USE_CHAT_GPT:
        chat_gpt_response = respond(message, processed_context)
    else:
        chat_gpt_response = "Here are few episodes that might be relevant to your question:"

    response = f"""
{chat_gpt_response}

Episode Title 1: {context[0]['info']['title']}
Episode Link 1: {context[0]['info']['link']}
Episode Title 2: {context[1]['info']['title']}
Episode Link 2: {context[1]['info']['link']}
Episode Title 3: {context[2]['info']['title']}
Episode Link 3: {context[2]['info']['link']}
Episode Title 4: {context[3]['info']['title']}
Episode Link 4: {context[3]['info']['link']}
Episode Title 5: {context[4]['info']['title']}
Episode Link 5: {context[4]['info']['link']}
"""
    return response

