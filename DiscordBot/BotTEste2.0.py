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

bot.run('Discord Token aqui')
