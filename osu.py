import discord
import json
import asyncio
import requests

apikey = "1ff00082bf0c95397f6bb245503be38f3ae7d96e"
root = "https://osu.ppy.sh/api/get_user?k=" + apikey

def get_user():
    user = requests.get(root + '&u=starrstyx')
    print(user.text)
    return