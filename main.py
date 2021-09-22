import nextcord
from nextcord.ext import commands, tasks

intents=nextcord.Intents.all()
client = commands.Bot(command_prefix = 'h!',intents=intents)

@client.event
async def on_ready():
	print('Bot is Online')

client.run("TOKEN")