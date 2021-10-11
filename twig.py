import twigcord 
import pymongo
import os
from twigcord import commands
from config import TOKEN
from config import DB_URI
from config import DEFAULT_PREFIX

client = twigcord.Client(command_prefix=DEFAULT_PREFIX, help_command=None)

@client.event
async def on_ready():
    print('TWIG FRONTEND LOADED')
    client.load_extension('src.fun')
    client.load_extension('src_hidden.automod')
    client.load_extension('src.moderation')

for filename in os.listdir('./src'):
  if filename.endswith('.py'):
    client.load_extension(f'src.{filename[:-3]}')
    
  else:
    print(f'Unable to load {filename[:-3]}')

for filename in os.listdir('./src_hidden'):
  if filename.endswith('.py'):
    client.load_extension(f'src_hidden.{filename[:-3]}')
    
  else:
    print(f'Unable to load {filename[:-3]}')

client.run(TOKEN)