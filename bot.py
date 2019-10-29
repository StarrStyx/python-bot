import discord

# bot token & client instance
token = "aaa"
client = discord.Client()
bot = commands.Bot(command_prefix='*')

@client.event
async def on_ready():
	print('logged on')



client.run(token)
