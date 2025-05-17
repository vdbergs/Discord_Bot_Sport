import discord
from discord import app_commands
from dotenv import load_dotenv
import os
import logging
import asyncio

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TOKEN')
APPLICATION_ID = os.getenv('APPLICATION_ID')
GUILD_ID = os.getenv('GUILD_ID')

# Validate environment variables
if not TOKEN or not APPLICATION_ID:
    logger.error("Missing TOKEN or APPLICATION_ID in .env")
    exit(1)
if GUILD_ID:
    logger.info(f"Using guild ID: {GUILD_ID}")
else:
    logger.info("No GUILD_ID provided, registering global commands")

# Initialize client and command tree
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Event: On ready
@client.event
async def on_ready():
    logger.info(f'Logged in as {client.user}')
    try:
        # Clear all global commands
        logger.info("Clearing global commands...")
        tree.clear_commands(guild=None)
        await asyncio.wait_for(tree.sync(guild=None), timeout=30.0)
        logger.info("Cleared all global commands.")

        # Clear guild-specific commands (if GUILD_ID is provided)
        if GUILD_ID:
            guild = discord.Object(id=GUILD_ID)
            logger.info(f"Clearing guild commands for guild {GUILD_ID}...")
            tree.clear_commands(guild=guild)
            await asyncio.wait_for(tree.sync(guild=guild), timeout=30.0)
            logger.info(f"Cleared all guild commands for guild {GUILD_ID}.")

        # Register new commands and sync
        logger.info("Registering new commands...")
        await asyncio.wait_for(tree.sync(guild=discord.Object(id=GUILD_ID) if GUILD_ID else None), timeout=30.0)
        logger.info("Registered new commands.")
    except asyncio.TimeoutError:
        logger.error("Command sync timed out after 30 seconds")
    except discord.HTTPException as e:
        logger.error(f"HTTP error during command sync: {e}")
    except discord.Forbidden as e:
        logger.error(f"Permission error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during command sync: {e}")
    finally:
        logger.info("Closing client...")
        await client.close()

# Run the client
try:
    client.run(TOKEN)
except продаж.InvalidToken:
    logger.error("Invalid TOKEN provided")
    exit(1)
except Exception as e:
    logger.error(f"Failed to run client: {e}")
    exit(1)