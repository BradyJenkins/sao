import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
Client = discord.Client()
client = commands.Bot(command_prefix = "-")
client.remove_command('help')
@client.event
async def on_ready():
    print("Bot is online and connected to Discord")
    await client.change_presence(game=discord.Game(name="play.megaplex.tk"))
@client.command(pass_context=True)
async def ip(ctx):
    embed=discord.Embed(title="Server Ip!", description="The Ip Is play.megaplex.tk", color=0xFCFF0F)
    await client.say(embed=embed)
client.run(os.getenv('TOKEN'))
