import discord
from discord.ext import commands
import setting
import message
import asyncio
import schedule

token = setting.token
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
    
async def send_alerm():
    daily_message_list = message.get_message_by_type('daily')
    
    if daily_message_list == []:
        return
    
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.name == setting.channel_name:
                for msg in daily_message_list:
                    await channel.send(msg)

@bot.event
async def on_ready():
    schedule.every().day.at('12:00').do(lambda: asyncio.create_task(send_alerm()))
    
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

@bot.command()
async def codeforces(ctx):
    if ctx.channel.name == setting.channel_name:
        await ctx.send(message.get_message_by_type('codeforces'))
    
@bot.command()
async def atcoder(ctx):
    if ctx.channel.name == setting.channel_name:
        await ctx.send(message.get_message_by_type('atcoder'))
    
@bot.command()
async def all(ctx):
    if ctx.channel.name == setting.channel_name:
        await ctx.send(message.get_message_by_type('all'))

bot.run(token)