import discord, asyncio
from discord.ext import commands

bt = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bt.event
async def on_ready(): print(f'On {bt.user}')

@bt.tree.command(name='404')
async def spam(i: discord.Interaction):
    await i.response.send_message("intosmoke", ephemeral=True)
    for _ in range(20):
        await i.followup.send("[/404 Pwned This](https://discord.gg/5WbtZedcwt)")
        await asyncio.sleep(0.1)

bt.run("") #Your bot token
