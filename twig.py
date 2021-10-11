import nextcord 
import pymongo
from nextcord import commands
from config import TOKEN
from config import DB_URI
from config import DEFAULT_PREFIX

client = nextcord.Client(command_prefix=DEFAULT_PREFIX, help_command=None)

@client.event
async def on_ready():
    print('TWIG FRONTEND LOADED')
    client.load_extension("src.fun")
    client.load_extension("src.moderation")
    client.load_extension("src.fun")
    client.load_extension("src.fun")

client.run(TOKEN)