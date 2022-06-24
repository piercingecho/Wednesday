#like to call it: Thursday
import datetime
import asyncio
from discord.ext import commands, tasks
import discord

class Asuka(commands.Cog):
    def __init__(self, bot, AnnounceChannel):
        self.bot = bot
        self.channelPlace = AnnounceChannel #AnnounceChannel passed as an int
        self.LikeToCall.start()

    def cog_unload(self):
        self.LikeToCall.cancel()

    @tasks.loop(minutes = 1)
    async def LikeToCall(self):
        print("Running loop")
        t = datetime.datetime.now()
        wkd = datetime.datetime.weekday(t)
        if(wkd == 5):
            if(t.hour == 22 and t.minute == 51):
                await bot.get_channel(channelPlace).send("i love cogs")
                print("Hi!")

        if(wkd == 3):
            if(t.hour == 23 and t.minute == 58):
                await bot.get_channel(channelPlace).send("It's Wednesday")
            elif(t.hour == 23 and t.minute == 59):
                await bot.get_channel(channelPlace).send("or as I like to call it,")
        elif(wkd == 4):
            if(t.hour == 0 and t.minute == 0):
                await bot.get_channel(channelPlace).send("Thursday")
                await bot.get_channel(channelPlace).send("https://cdn.discordapp.com/attachments/787188953539280906/989609455538831430/Feliz_Jueves.mp4")