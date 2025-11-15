import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import asyncio
from collections import deque

from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

keep_alive()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  await bot.tree.sync()
  print(f'Logged in as {bot.user} (ID: {bot.user.id}) is up')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await message.channel.send(f'Hello {message.author.mention}!')
    await bot.process_commands(message)

@bot.event
async def on_disconnect():
    print("Bot is disconnecting...")

bot.run(TOKEN)

