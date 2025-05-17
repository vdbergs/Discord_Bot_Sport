from discord.ext import commands
from discord import app_commands
import discord

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check if the bot is online")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)  # Convert to milliseconds
        await interaction.response.send_message(f'Pong! Latency: {latency}ms')

async def setup(bot):
    await bot.add_cog(General(bot))