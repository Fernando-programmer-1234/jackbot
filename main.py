import re
import discord
from discord.ext import commands
import json
import os

# IDs dos Canais
CANAL_INSTAGRAM = 1493752795902509268
CANAL_TIKTOK = 1493752830735941815

# padrões específicos
instagram_pattern = r"(instagram\.com)"
tiktok_pattern = r"(tiktok\.com)"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

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
    
    link_pattern = r"(https?://\S+|www\.\S+)"

    content = message.content.lower()

    if re.search(link_pattern, content):

        # ✅ LIBERAR Instagram no canal certo
        if message.channel.id == CANAL_INSTAGRAM and re.search(instagram_pattern, content):
            await bot.process_commands(message)
            return

        # ✅ LIBERAR TikTok no canal certo
        if message.channel.id == CANAL_TIKTOK and re.search(tiktok_pattern, content):
            await bot.process_commands(message)
            return

        # ❌ BLOQUEIA O RESTO
        await message.delete()
        await message.channel.send(
            f"{message.author.mention}, links não são permitidos aqui!",
            delete_after=5
        )

    await bot.process_commands(message) #MUITO IMPORTANTE!!!


TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("TOKEN não encontrado!")
    exit()

bot.run(TOKEN)
