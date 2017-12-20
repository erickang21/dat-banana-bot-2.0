import discord
import sys
import os
import io
import asyncio
from discord.ext import commands


class Utility:
    def __init__(self, bot):
       self.bot = bot
       
           
    @commands.command()
    async def ping(self, ctx):
        """Premium ping pong giving you a websocket latency."""
        color = discord.Color(value=0x00ff00)
        em = discord.Embed(color=color, title='PoIIIng! Your supersonic latency is:')
        em.description = f"{bot.latency * 1000:.4f} ms"
        em.set_footer(text="Psst...A heartbeat is 27 ms!")
        await ctx.send(embed=em)
        
        
    
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
            em.add_field(name='__Least Number__', value=a)
            em.add_field(name='__Greatest Number__', value=b)
            await ctx.send(embed=em)
            
                    
    @commands.command()
    async def rolldice(self, ctx):
        """Rolls a 6 sided die."""
        choices = ['1', '2', '3', '4', '5', '6']
        color = discord.Color(value=0x00ff00)
        em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
        await ctx.send(embed=em)
        
        
    @commands.command()
    async def textface(self, ctx, Type):
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
              
              
def setup(bot): 
    bot.add_cog(Utility(bot))               
