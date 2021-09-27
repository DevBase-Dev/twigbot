import nextcord
from nextcord.ext import commands

class Purge(commands.Cog):
  def __init__(self, client):
    self.client = client
    
    @commands.command(aliases=['clean','clear','Purge'])
    @commands.has_permissions(administrator=True)
    async def purge(ctx, limit: int):
      await ctx.channel.purge(limit=limit)
      await ctx.send('Cleared by {}'.format(ctx.author.mention),delete_after=5)
 

def setup(client):
  client.add_cog(Purge(client))
