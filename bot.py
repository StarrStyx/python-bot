import discord
from discord.ext import commands
from random import randint
from random import choice

TOKEN = ''

client = commands.Bot(command_prefix = '-')

#Called when bot is initially started.
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='with -cmdlist'))
    print('Hello Bot.')

#Help command
@client.command()
async def cmdlist():
    embedCMD = discord.Embed(
       #title = 'StarrBot Command List',
       description = '''Utilities: `roll` \nMisc.: `simon` `when` `finger` `fbi` `911`''',
       colour = discord.Colour.gold()
    )

    embedCMD.set_footer(text='For more enquires please contact StarrStyx#0526')
    embedCMD.set_author(name='List of commands:', icon_url='https://starrstyx.s-ul.eu/JxZ9upVu')
    await client.say(embed=embedCMD)

#Roll command
@client.command()
async def roll():
    #roll_no = randint(1,100)
    roll_no = randint(1,100)
    
    if roll_no >= 80:
        await client.say(':game_die: Good roll! You got {}.'.format(roll_no))
    if 50 <= roll_no < 80:
        await client.say(':game_die: Not too bad, you rolled a {}.'.format(roll_no))
    if 20 <= roll_no < 50:
        await client.say(":game_die: Kinda bad, that's a {}.".format(roll_no))
    if 1 < roll_no < 20:
        await client.say(':game_die: Rip, you only got {}.'.format(roll_no))
    if roll_no == 1:
        await client.say(':game_die: Are you Toy? You got {} lol.'.format(roll_no))
    #await client.say(':game_die: {}'.format(roll_no))

#Simon
@client.command()
async def simon():

    simonlist = ['https://media.discordapp.net/attachments/150208319871516673/377732157977919488/3.png', 'https://cdn.discordapp.com/attachments/150208512914489345/371419413821390868/2.png', 'https://cdn.discordapp.com/attachments/150208512914489345/371419288789188608/1.jpg']
    simonchoice = choice(simonlist)

    embedSimon = discord.Embed(
       title = ''
    )
    
    embedSimon.set_image(url=simonchoice)

    await client.say(embed=embedSimon)

#FBI command
@client.command()
async def fbi():
    embedFbi = discord.Embed(
       title = ''
    )
    
    embedFbi.set_image(url='https://cdn.discordapp.com/attachments/441576594419744778/499818180160520212/fbi_incoming.gif')

    await client.say(embed=embedFbi)

#When command
@client.command()
async def when():

    year = randint(2030,2300)
    month = randint(1,12)

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = randint(1,31)
    if month == 4 or month == 6 or month == 9 or month == 11:
        day = randint(1,30)
    if month == 2:
        if year%4 == 0:
            if year%100 == 0 and year%400 == 0:
                day = randint(1,29)
            if year%100 == 0 and year%400 != 0:
                day = randint(1,28)
            if year%100 != 0 and year%400 != 0:
                day = randint(1,29)
        if year%4 != 0:
            day = randint(1,28)        

    
    if month == 2 and year%4 == 0 and year%400 == 0:
        day = randint(1,29)
    if month == 2 and year%4 == 0 and year%400 != 0:
        day = randint(1,29)
    if month == 2 and year%4 != 0 and year%400 != 0:
        day = randint(1,28)

    await client.say('I think it will happen on {}/{}/{}.'.format(day, month, year))

#Finger command
@client.command()
async def finger():
    embedFinger = discord.Embed(
       title = ''
    )
    
    embedFinger.set_image(url=' https://i.imgur.com/Ynsu3T2.png')

    await client.say(embed=embedFinger)

@client.command(name="911")
async def _911():
    await client.say(""":fire: :fire: :fire: :airplane::fire: :fire: :fire: :fire: :fire: :fire:  :airplane: 
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃＼○／
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃   /
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃ノ)
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃   ＼○／
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃      /
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃   ノ)
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┗┛┗┛┗┛┃     ┃┗┛┗┛┗┛┃
┃┏┓┏┓┏┓┃     ┃┏┓┏┓┏┓┃
┃┃┃┃┃┃┃┃     ┃┃┃┃┃┃┃┃
┻┻┻┻┻┻┻┻     ┻┻┻┻┻┻┻┻ :police_car: :police_car: :police_car: :police_car: :police_car:""")

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