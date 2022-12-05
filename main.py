# bot.py
import os
import random
import discord
from time import sleep as zz
from dotenv import load_dotenv
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
global films
films=[]

def isearch(a):
    iq = imdb.IMDb()
    search = iq.search_movie(a)
    for movies in search:
        #print(movies)
        films.append(movies)

# this is just here to clear the terminal
@client.event
async def on_ready():
   s('clear')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Plex Discord server!'
    )

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('search'):
        await message.channel.send('What movie are you looking for: ')
        msg = await client.wait_for("message")
        film = msg.content  
        await message.channel.send(f'🔍{film}') # this will send out the message
        ##########

        isearch(film)
        for i in range(len(films)):
            await message.channel.send(f'[i+1] {films[i]}')
            zz(0.5)

        ##########
        #await message.channel.send()

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
