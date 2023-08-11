import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está online: {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'bom dia':
        await message.channel.send('Bom dia!')

    await bot.process_commands(message)

bot.run('MTExMTIzOTA4MzI4OTc1MTYwMg.GTy14C.YLwhhAjt_EZiHdJPN7qwEM47W4akm0i5nchm3k')