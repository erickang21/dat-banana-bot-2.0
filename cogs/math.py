import discord
import sys
import os
import io
from discord.ext import commands


class math:
    def __init__(self, bot):
       self.bot = bot
    
    
    @commands.command(aliases=['calculate', 'math'])
    async def calc(self, ctx, num: int, num2: int):
            '''Do those 4 simple operations with this bad boi.'''
            if num is None:
                await ctx.send("This command is currently under maintenace. Sorry bout that.")
            else:
                await ctx.send("This command is currently under maintenace. Sorry bout that.")
                await ctx.add_reaction("\U00002795")
                await ctx.add_reaction("\U00002796")
                await ctx.add_reaction("\U00002716")
                await ctx.add_reaction("\U00002797")
                
                
    @commands.command()
    async def add(self, ctx, num: int, num2: int):
        '''ADD EM UP! Yep.'''
        if num is None:
            await ctx.send("Aren't you stupid enough? Usage: *add [no.1] [no.2]")
        else:
            await ctx.send(num + num2)
                
                
    @commands.command()
    async def subtract(self, ctx, num: int, num2: int):
            '''That big MINUS. Usage: *subtract [no.1] [no.2]'''
            if num is None:
                await ctx.send("Aren't you stupid enough? Usage: *subtract [no.1] [no.2]")
            else:
                await ctx.send(num - num2)
                
                
    @commands.command()
    async def multiply(self, ctx, num: int, num2: int):
            '''Multiply em. Git ready! Usage: *multiply [no.1] [no.2]'''
            if num is None:
                await ctx.send("Aren't you stupid enough? Usage: *multiply [no.1] [no.2]")
            else:
                await ctx.send(num * num2)
                
                
    @commands.command()
    async def divide(self, ctx, num: int, num2: int):
            '''Divide em. Cut em. Idc. Usage: *multiply [no.1] [no.2]'''
            if num is None:
                await ctx.send("Aren't you stupid enough? Usage: *divide [no.1] [no.2]")
            else:
                await ctx.send(num / num2)
                
                
def setup(bot): 
    bot.add_cog(math(bot))  
