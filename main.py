import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
    
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hey {ctx.author.mention}, ready to write some code?")
    
    
@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    await ctx.send(
        f"**{guild.name}** — Members: `{guild.member_count}` | Channels: `{len(guild.channels)}`"
    )


bot.run(os.environ["DISCORD_BOT_TOKEN"])