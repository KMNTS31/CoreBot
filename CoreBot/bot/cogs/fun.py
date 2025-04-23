from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        jokes = ["Why don't skeletons fight? They don't have the guts.", "I'm reading a book on anti-gravity. It's impossible to put down!"]
        await ctx.send(random.choice(jokes))

def setup(bot):
    bot.add_cog(Fun(bot))
