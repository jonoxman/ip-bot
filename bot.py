import os
import discord
from dotenv import load_dotenv
import requests
import asyncio

#Constants
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members=True
intents.message_content=True

client = discord.Client(intents=intents)


async def ip_message_sender():
    """Send a message with the current IP of the host machine to a specified channel."""
    channel = client.get_channel(1266781996366041238) # Get the channel, the id has to be an int
    while True:
        ip = requests.get('https://api.ipify.org').text
        await channel.purge(limit=5)
        await channel.send('Current IP: ' + ip)
        await asyncio.sleep(86400)

@client.event
async def on_ready():
    '''On-startup trigger'''
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    await ip_message_sender()
    
client.run(TOKEN)
