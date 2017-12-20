import discord
import sys
import os
import io
import asyncio
from discord.ext import commands


class Math:
    def __init__(self, bot):
       self.bot = bot
                
    
    @commands.command()
    async def calc(self, ctx, num: int, num2: int):
        '''Be an Einstein! No wait, not you. The bot...'''
        if num is None:
            await ctx.send("Aren't you stupid enough? Usage: *calc [no.1] [no.2]")
        else:
            msg = await ctx.send("And...which operator? Use the reactions to select your choice. Choose from :heavy_plus_sign:, :heavy_minus_sign:, :heavy_multiplication_x:, :heavy_division_sign:.")
            await msg.add_reaction(':heavy_plus_sign:')
            await msg.add_reaction(':heavy_minus_sign:')
            await msg.add_reaction(':heavy_multiplication_x:')
            await msg.add_reaction(':heavy_division_sign:')
            
            def pred(reaction, user):
                return user == ctx.author and (str(reaction.emoji) == ':heavy_plus_sign:' or str(reaction.emoji) == ':heavy_minus_sign:' or str(reaction.emoji) == ':heavy_multiplication_x:' or str(reaction.emoji) == ':heavy_division_sign:)
    
            else:
                if str(reaction.emoji) == ':heavy_plus_sign:':                                   
                    await msg.delete()
                    color = discord.Color(value=0x00ff00)
                    em = discord.Embed(color=color, title: 'Calculation finished!')
                    em.description = f"{num} + {num2}   =   {num + num2}"
                    await ctx.send(embed=em)                           
                if str(reaction.emoji) == ':heavy_minus_sign:'
                    await msg.delete()
                    color = discord.Color(value=0x00ff00)
                    em = discord.Embed(color=color, title: 'Calculation finished!')
                    em.description = f"{num} - {num2}   =   {num - num2}"
                    await ctx.send(embed=em)   
                if str(reaction.emoji) == ':heavy_multiplication_x:'
                    await msg.delete()
                    color = discord.Color(value=0x00ff00)
                    em = discord.Embed(color=color, title: 'Calculation finished!')
                    em.description = f"{num} x {num2}   =   {num * num2}"
                    await ctx.send(embed=em)                              
                if str(reaction.emoji) == 'heavy_division_sign:'
                    await msg.delete()
                    color = discord.Color(value=0x00ff00)
                    em = discord.Embed(color=color, title: 'Calculation finished!')
                    em.description = f"{num} / {num2}   =   {num / num2}"
                    await ctx.send(embed=em)                              
 
                                               
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
    bot.add_cog(Math(bot))  
