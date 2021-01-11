import discord
from discord.ext import commands
import random
import os
import gogS

key=os.getenv('key')
wkey=os.getenv('wkey')

TOKEN = os.getenv('TOKEN')

gogLinks = gogS.get_gog("https://tenor.com/search/gog-gifs")

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def gog(ctx):
    await ctx.send( random.choice(gogLinks) )

@client.command()
async def ultimategog(ctx):
    await ctx.send('https://tenor.com/view/gog-ultimate-gog-ultigog-gog-monkey-monkey-gog-gif-18791701')

@client.command()
async def refreshgog(ctx):
    global gogLinks
    gogLinks = gogS.get_gog("https://tenor.com/search/gog-gifs")
    await ctx.send('refreshed gog')

client.run(TOKEN)
