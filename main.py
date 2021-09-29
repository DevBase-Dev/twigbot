import nextcord
from nextcord.ext import commands, tasks
from difflib import get_close_matches
import json
import os
import random
import pymongo
from pymongo import MongoClient
import aiohttp
import discord
from discord.ext import commands
##mongodb, PIP INSTALL PYMONGO, AND PIP INSTALL Python-DOTENV
##Make sure to have a mongodb server there free until 500mb

TOKEN = os.environ['TOKEN']

#MONGODB_URI = os.environ['MONGOURI']
#COLLECTION = os.getenv("COLLECTION")
#DB_NAME = os.getenv("DBNAME")

##COG LOADER
client=commands.Bot(command_prefix="h!")


##Change For Where Bot Is Actually Hosted
##For Economy

##When Will These Be Custom For Every Server? Or Are They Already?(VincentRPS)
PREFIX = 'h!'

intents=nextcord.Intents.all()
client = commands.Bot(command_prefix = PREFIX,intents=intents)

@client.event
async def on_ready():
  print('Bot is Online')

@client.event
async def on_member_join(member):
  with open('afk.json', 'r') as f:
    afk = json.load(f)
    
  await update_data(afk, member)  
    
  with open('afk.json','w') as f:
    json.dump(afk, f)
    
async def update_data(afk, user):
  if not f'{user.id}' in afk:
    afk[f'{user.id}'] = {}
    afk[f'{user.id}']['AFK'] = 'False'
    
@client.event
async def on_message(message):
  with open('afk.json','r') as f:
    afk = json.load(f)
    
  for x in message.mentions:
    if afk[f'{x.id}']['AFK'] = 'True':
      if message.author.bot:
        return
      em = nextcord.Embed(title='This User is afk!',description=f'You can\'t Ping {x} as he is AFK!',color=0x00FF00)
      await ctx.send(embed=em)
    
  if not message.author.bot:
    await update_data(afk, message.author)
    
    if afk[f'{message.author.id}']['AFK'] = 'True':
      NonEmbed = nextcord.Embed(description='I Have removed your AFK status!', color=0x00FF00)
      NonEmbed.set_author(name='You are no longer AFK!', icon_url=message.author.avatar.url)
      await message.channel.send(embed=NonEmbed)
      afk[f'{message.author.id}']['AFK'] = 'False'
      with open('afk.json', 'w') as f:
        json.dump(afk, f)
      await message.author.edit(nick=f'{message.author.display_name[5:]}')
      
  with open('afk.json', 'w') as f:
    json.dump(afk, f)
    
  await client.process_commands(message)
  
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      cmd = ctx.invoked_with
      cmds = [cmd.name for cmd in client.commands]
      matches = get_close_matches(cmd, cmds)
      if len(matches) > 0:
          embed = nextcord.Embed(title="Invalid Command!", description=f'Command `{str(PREFIX)}{cmd}` not found, maybe you meant `{str(PREFIX)}{matches[0]}`?')
          await ctx.send(embed=embed)
      else:
        embed = nextcord.Embed(title="Invalid Command!", description=f"Please type `{str(PREFIX)}help` to see all commands")
        await ctx.send(embed=embed)
      return
    if isinstance(error,commands.CommandOnCooldown):
      m, s = divmod(error.retry_after, 60)
      h, m = divmod(m, 60)
      if int(h) == 0 and int(m) == 0:
          em = nextcord.Embed(title="**Command on cooldown**", description=f'You must wait `{int(s)}` seconds to use this command!')
          await ctx.send(embed=em)
      elif int(h) == 0 and int(m) != 0:
          em = nextcord.Embed(title="**Command on cooldown**", description=f' You must wait `{int(m)}` minutes and `{int(s)}` seconds to use this command!')
          await ctx.send(embed=em)
      else:
          em = nextcord.Embed(title="**Command on cooldown**", description=f' You must wait `{int(h)}` hours, `{int(m)}` minutes and `{int(s)}` seconds to use this command!')
          await ctx.send(embed=em)
      return
    if isinstance(error, commands.DisabledCommand):
      em = nextcord.Embed(title='Command Disabled', description='It seems the command you are trying to use has been disabled')
      await ctx.send(embed=em)
      return
    if isinstance(error, commands.MissingPermissions):
      missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
      if len(missing) > 2:
          fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
      else:
          fmt = ' and '.join(missing)
      _message = 'You require the `{}` permission to use this command.'.format(fmt)
      em=nextcord.Embed(title='Invalid Permissions', description=_message)
      await ctx.send(embed=em)
      return
    if isinstance(error, commands.BotMissingPermissions):
      missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
      if len(missing) > 2:
          fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
      else:
          fmt = ' and '.join(missing)
      _message = 'I require the `{}` permission to use this command.'.format(fmt)
      em=nextcord.Embed(title='Invalid Permissions', description=_message)
      await ctx.send(embed=em)
      return
    if isinstance(error, commands.BadArgument):
      return
    print(error)
  
@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! | Speed: **{round(client.latency * 1000)}**ms')

@client.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes.json') as r:
            memes = await r.json()
            embed = discord.Embed(color=discord.Color.blue())
            embed.set_image(url=memes['data']['children'][random.randint(
                0, 25)]['data']['url'])
            embed.set_footer()
            await ctx.send(embed=embed)
            
@client.command()
async def afk(ctx, reason=None):
  if reason==None:
    await ctx.send('Please mention a reason!')
    return
  with open('afk.json','r') as f:
    afk=json.load(f)
    
  afk[f'{ctx.author.id}']['AFK'] = 'True'
  em = nextcord.Embed(,description='I Have set your status to AFK!', timestamp=ctx.message.created_at, color=0x00FF00)
  em.set_author(name='You are now AFK!',icon_url=ctx.author.avatar.url)
  em.add_field(name='Reason:', value=f'> {reason}')
  await ctx.send(embed=em)
    
  with open('afk.json', 'w') as f:
    json.dump(afk, f)
    
  await ctx.author.edit(nick=f'[AFK] {ctx.author.display_name}')
            
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
