import discord
import sys
import os
import io
from discord.ext import commands


class math:
    def __init__(self, bot):
       self.bot = bot
    
    
    @commands.command()
    async def add(self, ctx, num: int, num2: int):
            '''It...ADDS? Yea. Usage: *add [no.1] [no.2]'''
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
