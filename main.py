import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

channel_count = {}

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}!')

@bot.command()
async def startcount(ctx):
    channel_id = ctx.channel.id
    channel_count[channel_id] = 0
    await ctx.send("📈 カウントアップ開始！1から始めてください。")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author.bot:
        return

    channel_id = message.channel.id
    if channel_id in channel_count:
        try:
            number = int(message.content.strip())
        except ValueError:
            return

        expected = channel_count[channel_id] + 1
        if number == expected:
            channel_count[channel_id] = number
            await message.add_reaction('✅')
        else:
            await message.add_reaction('❌')
