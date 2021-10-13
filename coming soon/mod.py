import nextcord
from nextcord.ext import commands
import string, random

def getCaseNumber(): 
    numbers = []
    letters = []

    for i in range(6):
        numbers.append(str(random.randint(0, 9)))
        letters.append(random.choice(string.ascii_letters))

    return str(
      letters[0] + numbers[0] + letters[1] + numbers[1] + letters[2] + numbers[2] + 
      letters[3] + numbers[3] + letters[4] + numbers[4] + letters[5] + numbers[5]
    )

class mod(commands.Cog):
    def __init__(self, client):
      self.client = client

    @commands.commmand()
    async def kick(self,ctx,member:commands.MemberConverter, *, reason = None):
        if reason == None:
          reason = 'No reason provided'

        punishment_id = getCaseNumber()

        await member.kick(reason=reason)

        embed = nextcord.Embed(
        description = f':white_check_mark: Successfully kicked `{member}` with ID: `{punishment_id}`',
        color = nextcord.Color.from_rgb(250, 225, 225)
        )

        await ctx.send(embed=embed)

        @commands.commmand()
        async def ban(self,ctx,member:commands.MemberConverter, *, reason = None):
            if reason == None:
                reason = 'No reason provided'

            punishment_id = getCaseNumber()

            await member.ban(reason=reason)

            embed = nextcord.Embed(
            description = f':white_check_mark: Successfully kicked `{member}` with ID: `{punishment_id}`',
            color = nextcord.Color.from_rgb(250, 225, 225)
            )

            await ctx.send(embed=embed)

def setup(client):
  client.add_cog(mod(client))
