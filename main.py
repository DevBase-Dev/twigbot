import nextcord
from nextcord.ext import commands, tasks
from difflib import get_close_matches
import json
import os
import random
import pymongo
from pymongo import MongoClient
##mongodb, PIP INSTALL PYMONGO, AND PIP INSTALL Python-DOTENV
##Make sure to have a mongodb server there free until 500mb


MONGODB_URI = os.environ['MONGOURI']
COLLECTION = os.getenv("COLLECTION")
DB_NAME = os.getenv("DBNAME")

##COG LOADER
client=commands.Bot(command_prefix="h!")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension('cods.{filename{:-3}}')

##Change For Where Bot Is Actually Hosted
##For Economy
os.chdir(r"C:\\Users\ADMIN\Desktop\\helper-bot-main")

##When Will These Be Custom For Every Server? Or Are They Already?(VincentRPS)
PREFIX = 'h!'

intents=nextcord.Intents.all()
client = commands.Bot(command_prefix = PREFIX,intents=intents)

@client.event
async def on_ready():
	print('Bot is Online')
	
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

##Economy Start
##Remember To Add Send Money Stores And Items

async def open_account(user):
    with open("bank.json", "r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 100 

    with open("bank.json", "w") as f:
        json.dump(users,f) 
    return True         


async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)

    return users  

async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()   

    users[str(user.id)][mode] += change 
    
    with open("bank.json", "w") as f:
        json.dump(users,f) 
    
    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal      


@client.command(name="withdraw", aliases=["with"])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Hey Dumbo You Gotta WithDraw An Amount Duh")
        return
        
    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("Ayo You Poor ASF MAN!")
        return

    if amount<bal[0]:
        await ctx.send("You Want 0 Man stfu")
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount, "bank")

    await ctx.send(f"You Withdrew ${amount}!")

@client.command(name="deposit", aliases=["dep"])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Hey Dumbo You Gotta Deposit An Amount Duh")
        return
        
    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("Ayo You Poor ASF MAN!")
        return

    if amount<bal[0]:
        await ctx.send("You Want To Deposit $0 Man stfu")
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount, "bank")

    await ctx.send(f"You Deposited ${amount}!")


@client.event
async def on_ready():
    print("Economy Is Working Fine :EpicFace:")

@client.command(name="balance", aliases=["bal"])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]  
##Make Embeds More Cool lmao
    em = nextcord.Embed(title = f"{ctx.author.name}'s Balance", color = nextcord.Color.blue())
    em.add_field(name = "Wallet",value = wallet_amt)
    em.add_field(name = "Bank",value = bank_amt)
    await ctx.send(embed = em)


@client.command()
async def beg(ctx):
    await open_account(ctx.author)

    user = ctx.author
    
    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f"Someone Gave You ${earnings}!")
    
    users[str(user.id)]["wallet"] += earnings

    with open("bank.json", "w") as f:
        json.dump(users,f) 



##Economy End



client.run(TOKEN)

