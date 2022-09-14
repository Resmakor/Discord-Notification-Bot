import asyncio
import requests
import discord
from discord.ext import commands
import os

from dotenv import load_dotenv
load_dotenv()

token = os.environ['token']
bot_id = int(os.environ['bot_id'])
bot_prefix = ';'
channel_id = 944684218187911218

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix=bot_prefix, intents=intents)
client.remove_command("help")


client_id = os.environ['client_id']
client_secret = os.environ['client_secret']

channelNames = {
    'szymoool': 'false', 
    'franio': 'false', 
    'dawidssonek': 'false', 
    'annacramling': 'false', 
    'cinkrofwest': 'false', 
    'lukisteve': 'false',
    'rybsonlol_' : 'false',
    'arquel' : 'false',
    'vysotzky' : 'false',
    'xayoo_' : 'false',
    'japczan' : 'false',
    'lewus' : 'false',
    'kasix' : 'false',
    'gmpakleza' : 'false',
    'mamm0n' : 'false',
    'xntentacion' : 'false'
}


body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body)

keys = r.json()
headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']
}

@client.event
async def on_ready():
    print("Twitch Enjoyer is online")
    await job()

async def job():
    while True:
        channel = client.get_channel(channel_id)
        for streamer_name in channelNames:
            try:
                stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)
                stream_data = stream.json()
                await asyncio.sleep(3)
                
                if len(stream_data['data']) == 1 and channelNames[streamer_name] == 'false':
                    user = requests.get(f'https://api.twitch.tv/helix/users?login={streamer_name}', headers=headers)
                    user_info = user.json()
                    channelNames[streamer_name] = 'true'
                    game = stream_data['data'][0]['game_name']
                    description = f'**{streamer_name}** is live, playing {game}'
                    avatar = user_info['data'][0]['profile_image_url']
                    embed = discord.Embed(title='Update!', description=description, url=str(f'https://www.twitch.tv/{streamer_name}'), color=0xBF40BF)
                    embed.set_thumbnail(url=avatar)
                    await channel.send(embed=embed)

                elif len(stream_data['data']) != 1 and channelNames[streamer_name] == 'true':
                    user = requests.get(f'https://api.twitch.tv/helix/users?login={streamer_name}', headers=headers)
                    user_info = user.json()
                    channelNames[streamer_name] = 'false'
                    description = f'**{streamer_name}** stopped streaming!'
                    avatar = user_info['data'][0]['profile_image_url']
                    embed = discord.Embed(title='Update!', description=description, url=str(f'https://www.twitch.tv/{streamer_name}'), color=0xBF40BF)
                    embed.set_thumbnail(url=avatar)
                    await channel.send(embed=embed)
            except:
                print('Too many requests!')
            await asyncio.sleep(10)

@client.command()
async def streamers(ctx):
    channel = client.get_channel(channel_id)
    streamers = list(channelNames.keys())
    await channel.send(streamers)   

client.run(token)

