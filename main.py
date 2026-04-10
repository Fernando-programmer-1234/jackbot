import re
import discord
from discord.ext import commands
import json
import os

# carregar configurações
with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

# quando o bot estiver ligado
@bot.event
async def on_ready():
    print(f'{bot.user} está online!')

#comnando simples/teste
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

#ant-link
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    link_patter = r"(https?://\S+|www\.\S+)"

    if re.search(link_patter, message.content):
        await message.delete()
        await message.channel.send(
            f"{message.author.mention}, links não são permitidos aqui!",
            delete_after=5
        )

    await bot.process_commands(message) #MUITO IMPORTANTE!!!

bot.run(config['token'])
