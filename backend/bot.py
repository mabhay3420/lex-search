import discord
from gpt import generate_response
from creds import DISCORD_BOT_TOKEN, DISCORD_CLIENT_ID

# Declare the intents your bot will use
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)


async def send_response(response, channel):
    await channel.send(response)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    # Define the permission integer
    PERMISSIONS = discord.Permissions(send_messages=True, read_message_history=True)

    # Generate the OAuth2 URL with the specified permissions
    oauth_url = discord.utils.oauth_url(DISCORD_CLIENT_ID, permissions=PERMISSIONS)
    print(oauth_url) 

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # print("Full message content:", message)
    
    print("=====================================")
    print(f"{message.author} : {message.content}")
    response = await generate_response(message.content)
    print(f"Bot: {response}")
    print("=====================================")

    await send_response(response, message.channel)


def run_bot():
    client.run(DISCORD_BOT_TOKEN)

if __name__ == "__main__":
    run_bot()
