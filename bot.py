import discord
import json
import osu

# bot token & client instance
token = "var1"
client = discord.Client()
bot = commands.Bot(command_prefix='*')

@client.event
async def on_ready():
   print('logged on')

async def on_message(message):
    if 0 == 1:
        osu.get_user()

client.run(token)