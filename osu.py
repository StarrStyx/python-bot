import discord
import json
import asyncio
import requests

apikey = "1ff00082bf0c95397f6bb245503be38f3ae7d96e"
api_url = "https://osu.ppy.sh/api/get_user?k=" + apikey

def get_user(username):
    userdata = requests.get(api_url + '&u=starrstyx')
    output = json.loads(userdata.text)

    userdataEmbed = discord.Embed(title="sike")
    return userdataEmbed