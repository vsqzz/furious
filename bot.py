import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.all()  # Enable all intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event: Member joins the server
@bot.event
async def on_member_join(member):
    guild = member.guild  # Get the guild (server) where the member joined
    role = discord.utils.get(guild.roles, name="Members")  # Replace with your desired role name
    if role:
        await member.add_roles(role)
        print(f'{member.display_name} has joined and been given the role {role.name}.')
    else:
        print(f'The role "Members" was not found.')

# Command: Ping (just for testing)
@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  # Convert to ms
    await ctx.send(f'Pong! Latency: {latency:.2f}ms')

# Other commands...

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token
TOKEN = 'MTI1MzQ5Njc2ODEzODcwNzA0NQ.GW3E2d.5PgV3KIpBRAo84aORnxSW3Bj0pvSDNmGET-10g'

# Run the bot
bot.run(TOKEN)
