import discord
from discord.ext import commands
from random import randint

TOKEN = 'NDk5NjAyOTU1MjgwOTczODI1.DqA5Fg.-WBTGxdUhoM-nLJ-Xu8N_nbWbKE'

client = commands.Bot(command_prefix = '!!')

#Called when bot is initially started.
@client.event
async def on_ready():
    print('Hello Bot.')

#Help command
@client.command()
async def cmdlist():
    await client.say('```List of commands: (Prefix for commands is !!)\n\n- roll: Rolls random number between 1 and 100```')

#Roll command
@client.command()
async def roll():
    roll_no = randint(1,100)
    await client.say(':game_die: {}'.format(roll_no))



#@client.event
#async def on_message(message):
    #author = message.author
    #content = message.content
    #print('{}: {}'.format(author, content))

#@client.event
#async def on_message(message):
    #channel = message.channel
    #if message.content.startswith('.ping'):
    #    await client.send_message(channel, 'Pong!')

    #if message.content.startswith('.echo'):
        

#@client.event
#async def on_message_delete(message):
    #author = message.author
    #content = message.content
    #channel = message.channel
    #await client.send_message(channel, '{}: {}'.format(author, content))

client.run(TOKEN)