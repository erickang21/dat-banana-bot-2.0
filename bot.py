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
async def on_guild_join():
    lol = bot.get_channel(390255995768799245)
    em = discord.Embed(color=discord.Color(value=0x00ff00))
    em.title = "dat banana bot has arrived in a new server!"
    em.description = f"Server: {ctx.message.author.guild.name}"
    await lol.send(embed=em)


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
async def hack(ctx, msg:str):
    """Hack someone's account! Try it!"""
    msg = await ctx.send(f"Hacking! Target: {msg}")
    asyncio.sleep(3)
    await msg.edit(content="Accessing Discord Files... [▓▓    ]")
    asyncio.sleep(3)
    await msg.edit(content="Accessing Discord Files... [▓▓▓   ]")
    asyncio.sleep(3)
    await msg.edit(content="Accessing Discord Files... [▓▓▓▓▓ ]")
    asyncio.sleep(3)
    await msg.edit(content="Accessing Discord Files COMPLETE! [▓▓▓▓▓▓]")
    asyncio.sleep(3)
    await msg.edit(content="Retrieving Login Info... [▓▓▓    ]")
    asyncio.sleep(3)
    await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓ ]")
    asyncio.sleep(3)
    await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓▓ ]")
    asyncio.sleep(10)
    await msg.edit(content=f"An error has occurred hacking {msg}'s account. Please try again later. :x:")
    
        
        
@bot.command()
async def timer(ctx, timer):
    """Counts down till it's over! Usage: *timer [time in secs]"""
    try:
        float(timer)
    except ValueError:
        await ctx.send("UH OH! Timer did not start. Usage: *timer [time in secs]. Make sure the time is a *whole number*.")
    else:
        await ctx.send("Timer started and rolling! :timer:")
        await asyncio.sleep(float(timer))
        await ctx.send("TIME'S UP! :clock:")

        
@bot.command()
async def eightball(ctx, *, message:str):
    """Really desperate? Ask the 8ball for advice. Only yes/no questions!"""
    choices = ['It is certain. :white_check_mark:', 'It is decidedly so. :white_check_mark:', 'Without a doubt. :white_check_mark:', 'Yes, definitely. :white_check_mark:', 'You may rely on it. :white_check_mark:', 'As I see it, yes. :white_check_mark:', 'Most likely. :white_check_mark:', ' Outlook good. :white_check_mark:', 'Yes. :white_check_mark:', 'Signs point to yes. :white_check_mark:', 'Reply hazy, try again. :large_orange_diamond: ', 'Ask again later. :large_orange_diamond: ', 'Better not tell you now. :large_orange_diamond: ', 'Cannot predict now. :large_orange_diamond: ', 'Concentrate and ask again. :large_orange_diamond: ', 'Do not count on it. :x:', 'My reply is no. :x:', 'My sources say no. :x:', 'Outlook not so good. :x:', 'Very doubtful. :x:']
    color = discord.Color(value=0xeaff29)
    em=discord.Embed(color=color, title=f"{message}", description=random.choice(choices))
    em.set_author(name="8 ball!", icon_url="https://vignette.wikia.nocookie.net/battlefordreamislandfanfiction/images/5/53/8-ball_my_friend.png/revision/latest?cb=20161109021012")
    em.set_footer(text=f"Sent by {ctx.message.author.name}")
    await ctx.message.delete()
    await ctx.send(embed=em)
    
    
    
@bot.command()
async def say(ctx, *, message:str):
    '''I say what you want me to say. Oh boi...'''
    await ctx.message.delete()
    await ctx.send(message)                   
                       
        
@bot.command()
async def invite(ctx):
    """Allow my bot to join the hood. YOUR hood."""
    await ctx.send("Lemme join that hood -> https://discordapp.com/oauth2/authorize?client_id=388476336777461770&scope=bot&permissions=2146958591")                       

                       
@bot.command(name='discord')
async def _discord(ctx):
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

