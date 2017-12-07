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
