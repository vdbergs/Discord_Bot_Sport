from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name='clear',
        description='Delete a number of messages from the channel.'
    )
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx: commands.Context, amount: int):
        """Clears the specified number of messages."""
        if ctx.interaction:
            await ctx.interaction.response.defer(ephemeral=True)
        deleted = await ctx.channel.purge(limit=amount + 1)
        # For slash commands, use followup to send ephemeral confirmation
        if ctx.interaction:
            await ctx.interaction.followup.send(f"✅ Deleted {len(deleted)-1} messages.", ephemeral=True)
        else:
            await ctx.send(f"✅ Deleted {len(deleted)-1} messages.", delete_after=3)

    @clear.error
    async def clear_error(self, ctx, error):
        msg = None
        if isinstance(error, commands.MissingPermissions):
            msg = "❌ You need the 'Manage Messages' permission to use this command."
        elif isinstance(error, commands.MissingRequiredArgument):
            msg = "❌ Please enter the **number** of messages to delete. Usage: `/clear <amount>`"
        elif isinstance(error, commands.BadArgument):
            msg = "❌ Please provide a valid **number**. Usage: `/clear <amount>`"
        else:
            msg = f"❌ An error occurred: {error}"
        if ctx.interaction:
            await ctx.interaction.response.send_message(msg, ephemeral=True)
        else:
            await ctx.send(msg, delete_after=5)

async def setup(bot):
    await bot.add_cog(Clear(bot))