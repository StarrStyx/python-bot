import discord
from discord.ext import commands

TOKEN = 'NDk5NjAyOTU1MjgwOTczODI1.Dp-rcQ.xQJZXdC2oZ4WXs1MThzf0vqaQ_k'

client = commands.Bot(command_prefix = '!/')

@client.event
async def on_ready():
    print('Hello Bot.')

client.run(TOKEN)