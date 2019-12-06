import discord
from discord.ext import commands
import json
import osu

# bot token & client instance
token = "var1"
client = discord.Client()
bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='with -cmdlist'))
    print('logged on')

# fetch userdata
@bot.command
async def user(ctx,arg):
    userdata = await osu.get_user(arg)
    prinit(userdata.text)

@bot.event
async def getuserdata():
    osu.get_user()

@bot.event
async def on_message(message):
    if message.content.startswith('-hello'):
        await message.channel.send('hello!')

bot.run(token)

#osu.get_user("StarrStyx")