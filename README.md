# Discord Notification Bot "Twitch Enjoyer"

## Description

"Twitch Enjoyer" is a Discord Bot (made in Python) using Twitch API to send notifications, when some streamers started/stopped streaming. 

## File "requirements.txt"
File "requirements.txt" is a list with the libraries needed for the bot to work.

## File "Twitch_enjoyer.py"
At the beginning there is the initialization of the Discord bot with environment variables, prefix to cause commands, text channel's id and some intents to make it all work.
```python
# Discord API settings
token = os.environ['token']
bot_id = int(os.environ['bot_id'])
bot_prefix = ';'
channel_id = < your channel_id >
intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix=bot_prefix, intents=intents)
```
#
Later program initializes Twitch bot and dictionary ```channelNames``` with Twitch nicknames - keys and values - ```false```. 
```python
# Twitch API settings
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
    'xntentacion' : 'false'
}
```
#
Then there is initialization of request body and headers needed to receive information about streamers.
```python
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
```
#
```python
@client.event
async def on_ready():
```
- Function ```on_ready``` starts infinite loop ```job```.

```python
async def job():
    while True:
```
- In that infinite loop "Twitch Enjoyer":
- requests data, 
changes ```channelNames``` values from ```False``` to ```True``` and vice versa,
- reads specific information about streamers (game name, avatar),
- sends notification on Discord channel.

![alt text](https://github.com/Resmakor/Twitch_Enjoyer_Public/blob/main/snippets/How_it_works_1.png?raw=true)

#
```python
@client.command()
async def streamers(ctx):
```
- Function ```streamers``` sends list of keys in ```channelNames```.

![alt text](https://github.com/Resmakor/Discord-Notification-Bot/blob/main/snippets/How_it_works_2.png?raw=true)

#
## File "icon_detection.py"
File "icon_detection.py" includes only 1 function:
```python
def link(nickname):
```
I used it to detect link to streamer's avatar without Twitch API, just web scraping (similar idea to YouTube video's url regular expression). 

Result of this program depends on the size of the uploaded photo. I could improve this, however when I have access to Twitch API it is unnecessary. I added this file just as trivia ;).
