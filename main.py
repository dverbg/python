import discord
from discord.ext import commands
import os

BOT_TOKEN = os.environ['MTQ0MjE1ODMxMDAzNTAzNDE5NA.Gpg4Jc.WcQnDP00pLD6yd9u9z46FQGDWwQOujZoMj6JNo']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online!')

@bot.command()
async def test(ctx):
    await ctx.send("🤖 Bot is working!")

if __name__ == "__main__":
    bot.run(BOT_TOKEN)
