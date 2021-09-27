import nextcord
from nextcord.ext import commands

class say(commands.Cog):
    def __init__(self, client):
      self.client = client
    
    
    @commands.command()
    async def say(self, ctx, *,message=None):
      if message == None:
        await ctx.reply('Give me a word to say!')
      else:
        e=nextcord.Embed(description=message)
        e.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=e)
        
        
        
def setup(client):
  client.add_cog(say(client))
