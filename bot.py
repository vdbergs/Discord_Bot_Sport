import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: On ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        await bot.load_extension('cogs.example_cog')  # Add await here
        await bot.tree.sync(guild=discord.Object(id=os.getenv('GUILD_ID')) if os.getenv('GUILD_ID') else None)
        print("Commands synced.")
    except Exception as e:
        print(f"Error: {e}")

# Run the bot
bot.run(os.getenv('TOKEN'))