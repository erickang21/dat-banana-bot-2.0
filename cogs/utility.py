import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import pip
import random
import textwrap
from discord.ext import commands


class utility:
    def __init__(self, bot):
       self.bot = bot
       

    @commands.command()
    async def timer(self, ctx, timer):
        """Counts down till it's over! Usage: *timer [time in secs]"""
        try:
            float(timer)
        except ValueError:
            await ctx.send("UH OH! Timer did not start. Usage: *timer [time in secs]. Make sure the time is a *whole number*.")
        else:
            await ctx.send("Timer started and rolling! :timer:")
            await asyncio.sleep(float(timer))
            await ctx.send("TIME'S UP! :clock:")
        
        
    @commands.command()
    async def ranint(self, ctx, a: int, b: int):
        """Usage: *ranint [least number][greatest number]. RanDOM!"""
        if a is None:
            await ctx.send("Boi, are you random! Usage: *ranint [least #] [greatest #], to set the range of the randomized number. Please use integers.")
        if b is None:
            await ctx.send("Boi, are you random! Usage: *ranint [least #] [greatest #], to set the range of the randomized number. Please use integers.")
        else:
            color = discord.Color(value=0x00ff00)
            em = discord.Embed(color=color, title='Your randomized number:')
            em.description = random.randint(a,b)
            await ctx.send(embed=em)
            
                    
    @commands.command()
    async def rolldice(self, ctx):
        """Rolls a 6 sided die."""
        choices = ['1', '2', '3', '4', '5', '6']
        color = discord.Color(value=0x00ff00)
        em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
        await ctx.send(embed=em)
        
        
    @commands.command(aliases=['tf'])
    async def textface(self, ctx, Type):
        """Get those dank/cool faces here. Type *textface list for a list."""
        if Type is None:
            await ctx.send('That is NOT one of the dank textfaces in here yet. Use: *textface [lenny/tableflip/shrug]')
        else:
            if Type.lower() == 'lenny':
              await ctx.send('( ͡° ͜ʖ ͡°)')
            elif Type.lower() == 'tableflip':
              await ctx.send('(ノಠ益ಠ)ノ彡┻━┻')
            elif Type.lower() == 'shrug':
              await ctx.send('¯\_(ツ)_/¯')
            elif Type.lower() == 'bignose':
              await ctx.send('(͡ ͡° ͜ つ ͡͡°)')
            elif Type.lower() == 'iwant':
              await ctx.send('ლ(´ڡ`ლ)')
            elif Type.lower() == 'musicdude':
              await ctx.send('ヾ⌐*_*ノ♪')
            elif Type.lower() == 'list':
              color = discord.Color(value=0x00ff00)
              em = discord.Embed(color=color, title='List of Textfaces')
              em.description = 'Choose from the following: lenny, tableflip, shrug, bignose, iwant, musicdude. Type *textface [face].'
              em.set_footer(text="Don't you dare question my names for the textfaces.")
              await ctx.send(embed=em)
            else:
              await ctx.send('That is NOT one of the dank textfaces in here yet. Use *textface list to see a list of the textfaces.')
            
            
    @commands.command(aliases=['av'])
    async def avatar(self, ctx, user: discord.Member):
        """Returns a user's avatar url. Use *av [user], or just *av for your own."""
        if user is None:
            await ctx.send(ctx.message.author.avatar_url)                   
        else:
            await ctx.send(user.avatar_url)
        
              
              
def setup(bot): 
    bot.add_cog(utility(bot))               
