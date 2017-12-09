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
from contextlib import redirect_stdout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix='*',description="The revamped dat banana bot made by dat banana boi#1982.\n\nHelp Commands",owner_id=277981712989028353)
bot.load_extension("cogs.math")
bot.load_extension("cogs.mod")


def cleanup_code(content):
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
        await ctx.send('Want me to do something? YOU do it right first. Usage: *presence [game/stream] [msg]')

                       
@bot.command()
async def ping(ctx):
    """Premium ping pong giving you a websocket latency."""
    em = discord.Embed(title='PoIIIng! Your supersonic latency is:', description=f'{bot.latency * 1000:.4f} ms')
    await ctx.send(embed=em)
                       
                       
@bot.command()
async def textface(ctx, Type):
    """Get that lenny, tableflip, or shrug face in here!"""
    if Type is None:
        await ctx.send('That is NOT one of the dank textfaces in here yet. Use: *textface [lenny/tableflip/shrug]')
    else:
        if Type.lower() == 'lenny':
          await ctx.send('( ° ʖ °)')
        elif Type.lower() == 'tableflip':
          await ctx.send('(ノಠ益ಠ)ノ彡┻━┻')
        elif Type.lower() == 'shrug':
          await ctx.send('¯\_(ツ)_/¯')
        else:
          await ctx.send('That is NOT one of the dank textfaces in here yet. Use: *textface [lenny/tableflip/shrug]')
                       
                       
@bot.command()
async def say(ctx, *, message:str):
    '''I say what you want me to say. Oh boi...'''
    await ctx.message.delete()
    await ctx.send(message)                   
                       
        
@bot.command()
async def invite(ctx):
    """Allow my bot to join the hood. YOUR hood."""
    await ctx.send("Lemme join that hood -> https://discordapp.com/oauth2/authorize?client_id=388476336777461770&scope=bot&permissions=2146958591")                       

                       
@bot.command()
async def discord(ctx):
    """We have an awesome hood to join, join now!"""
    await ctx.send("Your turn to join the hood -> https://discord.gg/wvkVknA")
             
                       
@bot.command()
async def rolldice(ctx):
    """Rolls a 6 sided die."""
    choices = ['1', '2', '3', '4', '5', '6']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
    await ctx.send(embed=em)
                       
                       
@bot.command(hidden=True, name='eval')
async def _eval(ctx, *, body: str):

    if not dev_check(ctx.author.id):
        return

    env = {
        'bot': bot,
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    try:
        exec(to_compile, env)
    except Exception as e:
        return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        try:
            await ctx.message.add_reaction('\u2705')
        except:
            pass

        if ret is None:
            if value:
                await ctx.send(f'```py\n{value}\n```')
        else:
            await ctx.send(f'```py\n{value}{ret}\n```')    
                       
                       

if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))

