import discord
from discord.ext import commands
import asyncio

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

# Set your bot token here
TOKEN = 'MTIxMDI4NDExNDkxODUxNDczMA.Gdm3HE.jjk3BXkQzxKxmZmeerTjo6KRiQQum2gvIsWfY0'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

# remove the default help command so that we can write our own
bot.remove_command('help')

async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(TOKEN)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
