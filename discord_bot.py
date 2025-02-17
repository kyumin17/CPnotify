import discord
from discord.ext import commands
import setting
import message

token = setting.token
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def codeforces(ctx):
    await ctx.send(message.get_message('codeforces'))
    
@bot.command()
async def atcoder(ctx):
    await ctx.send(message.get_message('atcoder'))
    
@bot.command()
async def all(ctx):
    await ctx.send(message.get_message('all'))
    
bot.run(token)