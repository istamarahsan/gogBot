import discord
from discord.ext import commands
import random
import gogS

gogLinks = gogS.get_gog("https://tenor.com/search/gog-gifs")

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

@client.event
async def on_ready():
    print('Bot is ready.')

def is_it_me(ctx):
    return ctx.author.id == 326017514188308480

@client.command()
#@commands.check(is_it_me)
async def gog(ctx):
    await ctx.send( random.choice(gogLinks) )

@client.command()
#@commands.check(is_it_me)
async def ultimategog(ctx):
    await ctx.send('https://tenor.com/view/gog-ultimate-gog-ultigog-gog-monkey-monkey-gog-gif-18791701')

@client.command()
async def refreshgog(ctx):
    global gogLinks
    gogLinks = gogS.get_gog("https://tenor.com/search/gog-gifs")
    await ctx.send('refreshed gog')

client.run('Nzc3NTQzMjA2MTM2NDQ2OTc2.X7E9ig.EDrV9bidk2f8La4wXYZtcB7tpvo')
