import discord
from discord.ext import commands
import setting
import message
import asyncio
import schedule
import codeforces_data
import atcoder_data

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
            if setting.channel_name in channel.name:
                for msg in daily_message_list:
                    await channel.send(msg)

@bot.event
async def on_ready():
    await bot.tree.sync()
    
    schedule.every().day.at('12:00').do(lambda: asyncio.create_task(send_alerm()))
    schedule.every().day.at('04:00').do(codeforces_data.get_data)
    schedule.every().day.at('04:10').do(atcoder_data.get_data)
    
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

@bot.tree.command(name='codeforces', description='코드포스 대회 정보를 불러옵니다')
async def codeforces(interaction: discord.Interaction):
    await interaction.response.send_message(message.get_message_by_type('codeforces'))
    
@bot.tree.command(name='atcoder', description='앳코더 대회 정보를 불러옵니다')
async def atcoder(interaction: discord.Interaction):
    await interaction.response.send_message(message.get_message_by_type('atcoder'))
    
@bot.tree.command(name='all', description='코드포스 및 앳코더 대회 정보를 불러옵니다')
async def all(interaction: discord.Interaction):
    await interaction.response.send_message(message.get_message_by_type('all'))

bot.run(token)