from nextcord
from nextcord.ext import commands
import contextlib
import io

class eval(commands.Cog):
    def __init__(self, client):
    self.client = client


    @commands.command()
    async def eval(self,ctx, *,code):
      str_obj = io.StringIO()
      try:
          with contextlib.redirect_stdout(str_obj):
              exec(code)
      except Exception as e:
          em=nextcord.Embed(title="Output :",description=f"```{e.__class__.__name__}: {e}```")
          return await ctx.send(embed=em)
      e=nextcord.Embed(title="Output :",description=f'``{str_obj.getvalue()}``')
      await ctx.send(embed=e)
    
    
def setup(client):
  client.add_cog(eval(client))
