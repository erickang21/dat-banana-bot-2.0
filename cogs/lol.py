import discord
import os
import io
import sys
import asyncio
import aiohttp
from discord.ext import commands


class lol:
    def __init__(self, bot):
        self.bot = bot
        with open('data/apikeys.json') as f:
            lol = json.load(f)
            self.token = lol.get("lolapi")



    @commands.command()
    async def lolprofile(self, ctx, *, lolname:str):
        """Gets League of Legends stats! *lolprofile [name]"""
        try:    
            cass.set_riot_api_key(self.token)
            cass.set_default_region("NA")
            color = discord.Color(value=0xf1f442)
            summoner = cass.get_summoner(name=lolname)
            check = summoner.exists
            if check is False:
                return await ctx.send("Invalid LoL summoner name. :x:")
            em = discord.Embed(color=color, title=f'{summoner.name}')
            em.add_field(name='Summoner Level', value=f'{summoner.level}')
            em.add_field(name='Summoner ID', value=f'{summoner.id}')
            em.set_thumbnail(url=f'{summoner.profile_icon.url}')
            await ctx.send(embed=em)


def setup(bot): 
    bot.add_cog(lol(bot)) 
