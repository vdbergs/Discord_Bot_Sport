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
            try:
                await bot.load_extension(f'commands.{filename[:-3]}')
                print(f"[COG] Loaded: {filename}")
            except Exception as e:
                print(f"[COG-ERR] {filename}: {e}")

@bot.event
async def on_ready():
    print(f"[DEPLOY] Logged in as {bot.user}")
    await bot.tree.clear_commands(guild=None)
    print("[DEPLOY] Cleared all global slash commands.")
    synced = await bot.tree.sync()
    print(f"[DEPLOY] Synced {len(synced)} slash commands.")
    await bot.close()

async def main():
    await load_cogs()
    await bot.start(TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"[DEPLOY-ERR] {e}")