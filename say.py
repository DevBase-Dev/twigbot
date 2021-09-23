import nextcord
from nextcord.ext import commands

class say(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command()
    async def say(self, ctx, arg=None):
      if arg == None:
        await ctx.reply('Give me a word to say!')
      else:
        e=nextcord.Embed(description=arg)
        e.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=e)
        
        
        
def setup(client):
  client.add_cog(say(client))
