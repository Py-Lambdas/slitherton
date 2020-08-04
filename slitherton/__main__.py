from pathlib import Path

from decouple import config
from discord.ext import commands

ROOT_DIR = Path(__file__).resolve(strict=True).parent

bot = commands.Bot(command_prefix=config("DISCORD_PREFIX"))


@bot.event
async def on_ready():
    print("Slitherton has slithered in")


@bot.command()
async def ping(ctx):
    await ctx.send("PONG")


# Register Cogs with bot (disabled for now as there are no cogs)
# for cog in (ROOT_DIR / "cogs").glob("*.py"):
#     bot.add_cog(f"cogs.{cog}")

bot.run(config("DISCORD_BOT_KEY"))
