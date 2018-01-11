import discord
import sys
import os
import io
import asyncio
import aiohttp
import random
import subprocess
from discord.ext import commands


class developer:
    def __init__(self, bot):
       self.bot = bot
       
       
       
    @commands.command()
    async def restart(self, ctx):
        """Makes the bot shut UP and then shut DOWN, then start up again."""
        if not dev_check(ctx.author.id):
            return await ctx.send("HALT! This command is for the devs only. Sorry. :x:")
        msg = await ctx.send("Shutting down...")
        await asyncio.sleep(1)
        await msg.edit(content="Goodbye! :wave:")
        await bot.logout()
        
        
    @commands.command()
    async def changename(self, ctx, name:str):
        """Changes my name. Please make it good!"""
        if not dev_check(ctx.author.id):
            return await ctx.send("HALT! This command is for the devs only. Sorry. :x:")
        if name is None:
            return await ctx.send("Hmm...my name cannot be blank!")
        else:
            await self.bot.user.edit(username=name)


    @commands.command()
    async def exec(self, ctx, code):
        """Executes code like Command Line."""
        if not dev_check(ctx.author.id):
            return await ctx.send("HALT! This command is for the devs only. Sorry. :x:")
        await ctx.send(subprocess.run(f"{code}",stdout=subprocess.PIPE).stdout.decode('utf-8'))
            
            

def setup(bot): 
    bot.add_cog(developer(bot))   
    
