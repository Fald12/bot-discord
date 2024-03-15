import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import gen_emodji

with open("token.txt", "r") as f: # Membaca token dari file token.txt
    token = f.read() # Menyimpan token ke dalam variable token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def passwd(ctx):
    await ctx.send(gen_pass(5))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run(token)