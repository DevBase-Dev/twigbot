import nextcord
from nextcord.ext import commands

class Slowmode(commands.Cog):
    def __init__(self, client):
      self.client = client
    
    
    @commands.command(case_insensitive=True)
    async def slowmode(self, ctx, time:int):
      if (not ctx.author.guild_permissions.manage_messages):
          await ctx.send('Cannot run command! Requires: ``Manage Messages``')
          return
      if time == 0:
          await ctx.send('Slowmode is currently set to `0`')
          await ctx.channel.edit(slowmode_delay = 0)
      elif time > 21600:
          await ctx.send('You cannot keep the slowmode higher than 6 hours!')
          return
      else:
          await ctx.channel.edit(slowmode_delay = time)
          await ctx.send(f"Slowmode has been set to `{time}` seconds!")
        
def setup(client):
  client.add_cog(Slowmode(client))
