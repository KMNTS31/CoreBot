import discord
from discord.ext import commands
import os
from config import TOKEN

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Load all cogs from the cogs folder
for filename in os.listdir("./bot/cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"bot.cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name} | ID: {bot.user.id}")

bot.run(TOKEN)
