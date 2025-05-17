import discord
from discord.ext import commands
import os
import sys
from dotenv import load_dotenv
import asyncio

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables
load_dotenv()

# Bot setup with slash commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Load cogs
async def load_cogs():
    for filename in os.listdir('./bot/cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            await bot.load_extension(f'bot.cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Error syncing commands: {e}')

async def main():
    await load_cogs()
    await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    asyncio.run(main())