import discord
import random
import os
from discord.ext import commands
import asyncio

with open("token.txt", "r") as f: # Membaca token dari file token.txt
    token = f.read() # Menyimpan token ke dalam variabel token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Database resep sederhana
resep = {
    'pisang': 'Pisang yang sudah matang dapat dijadikan smoothie atau pisang goreng.',
    'roti': 'Roti yang sudah keras bisa dijadikan roti panggang atau roti tawar.',
    'sisa nasi': 'Sisa nasi bisa dijadikan nasi goreng atau bola-bola nasi.',
    'sayuran': 'Sisa sayuran bisa dijadikan sup atau tumis sayuran.',
    # Dapat menambahkan resep lain sesuai kebutuhan
}

# Database ide kerajinan dari plastik
kerajinan_plastik = {
    'botol': "1. Potong bagian atas botol plastik.\n2. Gunakan bagian bawah sebagai pot untuk tanaman.\n3. Gunakan bagian atas sebagai wadah penyimpanan kecil.",
    'gelas': "1. Bersihkan dan keringkan gelas plastik.\n2. Cat atau hias gelas plastik dengan pola-pola menarik.\n3. Gunakan sebagai tempat pensil atau alat tulis lainnya.",
    'kantong': "1. Lipat dan ikat kantong plastik untuk membuat tali yang kuat.\n2. Gunakan tali tersebut untuk membuat kerajinan rajutan seperti tas atau alas duduk.",
    # Dapat menambahkan lebih banyak ide kerajinan dari plastik
}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')


    
@bot.command("saran")
async def saran_daur_ulang(ctx, item: str):
    # Daftar barang yang bisa didaur ulang
    daur_ulang = ['kertas', 'kardus', 'botol plastik', 'kaleng', 'kaca']
    
    # Jika item ada dalam daftar daur_ulang, beri saran untuk mendaur ulang
    if item.lower() in daur_ulang:
        await ctx.send(f"Baiklah! {item.capitalize()} sebaiknya didaur ulang.")
    else:
        await ctx.send(f"Baiklah! {item.capitalize()} bisa dibuang ke tempat sampah biasa.")

@bot.command("resep")
async def resep_daur_ulang(ctx, item: str):
    # Mengecek apakah item ada dalam database resep
    if item.lower() in resep:
        await ctx.send(f"Rekomendasi untuk mengolah {item.capitalize()}: {resep[item.lower()]}")
    else:
        await ctx.send(f"Maaf, resep untuk mengolah {item.capitalize()} tidak ditemukan.")

@bot.command("ide_kreatif")
async def ide(ctx, item: str):
    # Mengecek apakah ide kerajinan tersedia untuk item tertentu
    if item.lower() in kerajinan_plastik:
        await ctx.send(f"Ide untuk membuat kerajinan dari {item.capitalize()}:\n{kerajinan_plastik[item.lower()]}")
    else:
        await ctx.send(f"Maaf, ide untuk membuat kerajinan dari {item.capitalize()} tidak ditemukan.")

bot.run(token)