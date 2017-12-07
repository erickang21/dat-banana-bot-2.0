import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import aiohttp
import pip
import random
import textwrap
from contextlib import redirect st_dout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix='*',description="The revamped dat banana bot made by dat banana boi#1982.\n\nHelp Commands",owner_id=277981712989028353)
bot.load_extension("cogs.math")
bot.load_extension("cogs.mod")


def cleanup_code(content)
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')
    
    
@bot.event
async def on_ready():
print('Bot is online!')

def dev_check(id):
    with open('data/devs.json') as f:
        devs = json.load(f)
    if id in devs:
        return True
    return False
    
    
@bot.event
async def on_guild_join(guild):
    print("Banana has joined a new guild: {}".format(guild.name))
    
    
@bot.event
async def on_ready():
        """Shows bot's status"""
        print("Logged in as:")
        print("Name : {}".format(bot.user.name))
        print("ID : {}".format(bot.user.id))
        print("----------------")
        server = len(bot.guilds)
        users = sum(1 for _ in bot.get_all_members())
        while 1==1:
            await bot.change_presence(game=discord.Game(name='with {} servers'.format(server)))
            await asyncio.sleep(10)
            await bot.change_presence(game=discord.Game(name='with {} users'.format(users)))
            await asyncio.sleep(10)                         
            await bot.change_presence(game=discord.Game(name='PREFIX = *'))
            await asyncio.sleep(10)
            await bot.change_presence(game=discord.Game(name='*help | *invite'))
            await asyncio.sleep(10)
            await bot.change_presence(game=discord.Game(name='Banana bot!'))
            await asyncio.sleep(25)
            
            
@bot.command(name='presence')
@commands.is_owner()
async def _set(ctx, Type=None,*,thing=None):
    """What AM I doing?!?!?!"""
    if Type is None:
        await ctx.send('Do it right, plz! Usage: *presence [game/stream] [msg]')
    else
