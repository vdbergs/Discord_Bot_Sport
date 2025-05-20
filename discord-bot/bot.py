import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

async def load_cogs():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')

@bot.event
async def on_ready():
    check = "✅"
    print(f'{check} Bot connected as {bot.user} {check}')
    print("Registered commands:")
    for command in bot.commands:
        print(f' - {command.name}')
    # Force sync application (slash) commands
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} slash commands.")

async def main():
    await load_cogs()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())