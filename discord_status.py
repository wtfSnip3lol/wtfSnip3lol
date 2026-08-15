"""
Discord Status Update Script
Update your Discord status programmatically
"""

import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
STATUS_MESSAGE = "🚀 Building awesome things!"  # Change this
STATUS_TYPE = discord.ActivityType.watching  # Options: playing, streaming, listening, watching

# Bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    update_status.start()

@tasks.loop(minutes=5)  # Update every 5 minutes
async def update_status():
    """Update the bot's status"""
    activity = discord.Activity(
        type=STATUS_TYPE,
        name=STATUS_MESSAGE
    )
    await bot.change_presence(activity=activity, status=discord.Status.online)
    print(f"📊 Status updated: {STATUS_MESSAGE}")

# Run the bot
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
