from nextcord import client
from nextcord.ext import commands
import string, random

class mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.commmand()
    async def kick(self,ctx,member:commands.MemberConverter, *, reason = None):
        if reason == None:
          reason = 'No reason provided'

        number1 = random.randint(0, 9)
        number2 = random.randint(0, 9)
        number3 = random.randint(0, 9)
        number4 = random.randint(0, 9)
        number5 = random.randint(0, 9)
        
        letter1 = random.choice(string.ascii_letters)
        letter2 = random.choice(string.ascii_letters)
        letter3 = random.choice(string.ascii_letters)
        letter4 = random.choice(string.ascii_letters)
        letter5 = random.choice(string.ascii_letters)

        punishment_id = f'{letter1}{number1}{letter2}{number2}{letter3}{number3}{letter4}{number4}{letter5}{number5}'

        await member.kick(reason=reason)

        embed = nextcord.Embed(
        description = f':white_check_mark: Successfully kicked `{member}` with ID: `{punishment_id}`',
        color = nextcord      .Color.from_rgb(250, 225, 225)
        )

        await ctx.send(embed=embed)

        @commands.commmand()
        async def ban(self,ctx,member:commands.MemberConverter, *, reason = None):
            if reason == None:
                reason = 'No reason provided'

            number1 = random.randint(0, 9)
            number2 = random.randint(0, 9)
            number3 = random.randint(0, 9)
            number4 = random.randint(0, 9)
            number5 = random.randint(0, 9)
            
            letter1 = random.choice(string.ascii_letters)
            letter2 = random.choice(string.ascii_letters)
            letter3 = random.choice(string.ascii_letters)
            letter4 = random.choice(string.ascii_letters)
            letter5 = random.choice(string.ascii_letters)

            punishment_id = f'{letter1}{number1}{letter2}{number2}{letter3}{number3}{letter4}{number4}{letter5}{number5}'

            await member.ban(reason=reason)

            embed = nextcord.Embed(
            description = f':white_check_mark: Successfully kicked `{member}` with ID: `{punishment_id}`',
            color = nextcord.Color.from_rgb(250, 225, 225)
            )

            await ctx.send(embed=embed)

def setup(client):
  client.add_cog(mod(client))
