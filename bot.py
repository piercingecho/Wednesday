import discord
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from oraseye import Asuka

#environments

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ANNOUNCE_CHANNEL = os.getenv('ANNOUNCE_CHANNEL')

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    bot.add_cog(Asuka(bot,int(ANNOUNCE_CHANNEL)))
    print("Bot is running now!")

bot.run(TOKEN)