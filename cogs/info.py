import nextcord
from nextcord.ext import commands
import platform


class Info(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def info(self, ctx):
    pythonVersion = platform.python_version()
    nextcordVersion = nextcord.__version__
    serverCount = len(self.client.guilds)
    memberCount = len(set(self.client.get_all_members()))

    embed = nextcord.Embed(
      title=f"{self.client.user.name} Stats",
      description="\uFEFF",
      colour=ctx.author.colour,
      timestamp=ctx.message.created_at,
    )

    embed.add_field(name="Bot Version:", value="0.2.0.0")
    embed.add_field(name="Python Version:", value=pythonVersion)
    embed.add_field(name="Nextcord Version", value=nextcordVersion)
    embed.add_field(name="Total Guilds:", value=serverCount)
    embed.add_field(name="Total Users:", value=memberCount)
    embed.add_field(name="Bot Developers:", value="<@740637592713691217> | <@760325335777804340> | <@751405982562648146> | <@697323031919591454> | <@744715959817994371>")
    embed.set_footer(text = f"[Support Server](https://nextcord.gg/ZsZQ4SHsqs)")

    embed.set_footer(text=f"Carpe Noctem | {self.client.user.name}")

    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Info(client))