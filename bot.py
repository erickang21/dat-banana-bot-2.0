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
    else:
      if Type.lower() == 'stream':
        await bot.change_presence(game=discord.game(name=thing,type=1,url='https://www.twitch.tv/a'),status='online')
        await ctx.send(f'Aye aye, I am now streaming {thing}!')
      elif Type.lower() == 'game':
        await bot.change_presence(game=discord.game(name=thing))
        await ctx.send(f'Aye aye, I am now playing {thing}!')
      elif Type.lower() == 'clear':
        await bot.change_presence(game=None)
        await ctx.send('Aye aye, I am not playing anything, anymore!')
      else:
        await ctx.send('Want me to do something? YOU do it right first. Usage: *presence [game/stream] [msg]

                       
@bot.command()
async def ping(ctx):
    """Websocket latency, delivered thru the finest ping pong."""
    em = discord.Embed(color=discord.Color(value=0x00ff00))
    em.title = "PoIIIng! Your supersonic latency is:"
    em.description = "f'{bot.ws.latency * 1000:.4f} ms'
    await ctx.send(embed=em)
                       
                       
@bot.command()
async def textface(ctx, Type)
    "Get that lenny, tableflip, or shrug face in here!"
    if Type is None:
        await ctx.send('That is NOT one of the dank textfaces in here yet. Use: *textface [lenny/tableflip/shrug]')
    else:
        if Type.lower() == 'lenny'
          await ctx.send('( ° ʖ °)')
        elif Type.lower() == 'tableflip'
          await ctx.send('(ノಠ益ಠ)ノ彡┻━┻')
        elif Type.lower() == 'shrug'
          await ctx.send('¯\_(ツ)_/¯')
        else
          await ctx.send('That is NOT one of the dank textfaces in here yet. Use: *textface [lenny/tableflip/shrug]')
                       
                       
@bot.command()
async def say(ctx, *, message:str)
    '''I say what you want me to say. Oh boi...'''
    await ctx.message.delete()
    await ctx.send(message)                   
                       
        
@bot.command()
