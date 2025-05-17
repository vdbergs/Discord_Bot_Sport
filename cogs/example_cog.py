from discord.ext import commands
from discord import app_commands, Interaction
import random

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Says Hello, World!")
    async def hello(self, interaction: Interaction):
        await interaction.response.send_message("Hello, World!")

    @app_commands.command(name="roll", description="Roll dice (e.g., 2d6 for two six-sided dice)")
    @app_commands.describe(dice="Format: NdM (e.g., 2d6 for two six-sided dice)")
    async def roll(self, interaction: Interaction, dice: str):
        try:
            # Parse input (e.g., "2d6" -> 2 dice, 6 sides)
            num_dice, num_sides = map(int, dice.lower().split('d'))
            if num_dice < 1 or num_dice > 100:
                await interaction.response.send_message("Number of dice must be between 1 and 100.", ephemeral=True)
                return
            if num_sides < 2 or num_sides > 100:
                await interaction.response.send_message("Number of sides must be between 2 and 100.", ephemeral=True)
                return

            # Roll dice
            results = [random.randint(1, num_sides) for _ in range(num_dice)]
            total = sum(results)
            result_str = f"Rolled {dice}: {results} (Total: {total})"
            await interaction.response.send_message(result_str)
        except ValueError:
            await interaction.response.send_message("Invalid format. Use NdM (e.g., 2d6).", ephemeral=True)

    @app_commands.command(name="clear", description="Clear a specified number of messages")
    @app_commands.describe(amount="Number of messages to delete (1-100)")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: Interaction, amount: int):
        if amount < 1 or amount > 100:
            await interaction.response.send_message("Amount must be between 1 and 100.", ephemeral=True)
            return

        # Defer response since purging might take time
        await interaction.response.defer(ephemeral=True)
        try:
            # Purge messages (limit includes the command message)
            deleted = await interaction.channel.purge(limit=amount + 1)
            await interaction.followup.send(f"Deleted {len(deleted) - 1} message(s).", ephemeral=True)
        except discord.Forbidden:
            await interaction.followup.send("I don't have permission to delete messages.", ephemeral=True)
        except Exception as e:
            await interaction.followup.send(f"Error: {e}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Example(bot))