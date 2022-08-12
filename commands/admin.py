import traceback
from typing import Optional, Literal

import discord
from discord import Object
from discord.ext import commands
from discord.ext.commands import bot, Context, Greedy


class Admin(commands.Cog, name="ADMIN_TOOLS"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: Context, guilds: Greedy[Object], spec: Optional[Literal["~"]] = None) -> None:
        if not guilds:
            if spec == "~":
                fmt = await ctx.bot.tree.sync(guild=ctx.guild)
            else:
                fmt = await ctx.bot.tree.sync()

            await ctx.send(
                f"Synced {len(fmt)} commands {'globally' if spec is not None else 'to the current guild.'}"
            )
            return

        assert guilds is not None
        fmt = 0
        for guild in guilds:
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException:
                traceback.print_exc()
            else:
                fmt += 1

        await ctx.send(f"Synced the tree to {fmt}/{len(guilds)} guilds.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))
