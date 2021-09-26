import nextcord
from nextcord.ext import commands 

class Avatar(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  #Command
  @commands.command(aliases=['av','pfp'])
  async def avatar(self, ctx, member:nextcord.Member = None):
    if member == None:
      member = ctx.author
    
    memberAvatar = member.avatar.url
    em = nextcord.Embed(title=f'{member.tag}\'s Avatar!', timestamp=ctx.message.created_at)
    em.set_image(url=memberAvatar)
    
    await ctx.send(embed=em)
    
def setup(client):
  client.add_cog(Avatar(client))
