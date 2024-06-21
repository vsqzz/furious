import discord
from discord.ext import commands
import random
import requests
import os

intents = discord.Intents.all()  # Enable all intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  # Convert to ms
    await ctx.send(f'Pong! Latency: {latency:.2f}ms')

# Your other commands...

# Automatically assign role to new members
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='members')
    if role:
        await member.add_roles(role)
    await member.send(f'Welcome to the server, {member.name}!')

# Fetch token from environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Run the bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("Bot token not found. Please set the DISCORD_BOT_TOKEN environment variable.")
