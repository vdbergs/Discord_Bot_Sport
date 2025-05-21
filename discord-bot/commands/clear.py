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
        if ctx.interaction:
            await ctx.interaction.response.defer(ephemeral=True)
        deleted = await ctx.channel.purge(limit=amount + 1)
        msg = f"✅ Deleted {len(deleted)-1} messages."
        if ctx.interaction:
            await ctx.interaction.followup.send(msg, ephemeral=True)
        else:
            await ctx.send(msg, delete_after=3)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            msg = "❌ You need the 'Manage Messages' permission."
        elif isinstance(error, commands.MissingRequiredArgument):
            msg = "❌ Enter the **number** of messages. `/clear <amount>`"
        elif isinstance(error, commands.BadArgument):
            msg = "❌ Provide a valid **number**. `/clear <amount>`"
        else:
            msg = f"❌ Error: {error}"
        if ctx.interaction:
            await ctx.interaction.response.send_message(msg, ephemeral=True)
        else:
            await ctx.send(msg, delete_after=5)

async def setup(bot):
    await bot.add_cog(Clear(bot))