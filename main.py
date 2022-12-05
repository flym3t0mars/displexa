# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from time import sleep
from os import system as s
import imdb

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

down='☑️'
complete='✅'

#############
# KEY WORDS #
#############

a='add '
null='[]'

@client.event
async def isearch(a):
    iq = imdb.IMDb()
    search = iq.search_movie(a)
    for movies in search:
        print(movies)

@client.event
async def on_ready():
    s('clear')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} has connected to Discord!\n'
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    sleep(1.5)
    s('clear')
    print('Current Members \n')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    sleep(1)
    s('clear')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if a in message.content.lower():
        split_=f'{message.content.split(a,len(message.content))[1:len(message.content)]}'
        mess=(''.join(split_))
        response=f"downloading: \n{down} {mess}"
        await message.channel.send(response)

        logging=print(mess)
        if logging!=null:
            logging

        with open('movieRequests.log', 'a') as f:
            f.write(str(message.author)+': '+mess+'\n')

client.run(TOKEN)