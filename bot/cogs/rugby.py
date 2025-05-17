from discord.ext import commands
from discord import app_commands
import discord
from scraper.sports.rugby import scrape_rugby_fixtures
from storage.database import Database

class Rugby(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @app_commands.command(name="rugby_fixtures", description="Get upcoming rugby fixtures")
    async def rugby_fixtures(self, interaction: discord.Interaction):
        await interaction.response.defer()  # Defer response for long tasks
        try:
            fixtures = scrape_rugby_fixtures()
            self.db.store_fixtures('rugby', fixtures)
            response = "Upcoming Rugby Fixtures:\n"
            for fixture in fixtures[:5]:  # Limit to 5 for brevity
                response += f"{fixture['date']}: {fixture['teams']} ({fixture['competition']})\n"
            await interaction.followup.send(response or "No fixtures found.")
        except Exception as e:
            await interaction.followup.send(f"Error fetching fixtures: {str(e)}")

async def setup(bot):
    await bot.add_cog(Rugby(bot))