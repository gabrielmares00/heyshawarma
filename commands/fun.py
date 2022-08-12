import discord
from discord import app_commands
from discord.ext import commands


class Fun(commands.Cog, name="FUN_TOOLS"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="ping")
    async def ping(self, ctx):
        if ctx.interaction:
            await ctx.interaction.response.send_message("Pong!")
        else:
            await ctx.send("Pong!")

    @app_commands.command(name="test-slash")
    async def my_command(self, interaction: discord.Interaction):
        await interaction.response.send_message("This is a pure slash command, also ephemeral", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))
