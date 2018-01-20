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
import cassiopeia as cass
from cassiopeia import Summoner


class lol:
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def lolprofile(self, ctx, lolname:str):
    	"""Gets League of Legends stats! Usage: *lolprofile [summoner name]"""
    	cass.set_riot_api_key('RGAPI-338c02bc-134d-4055-b846-41045a553b9b')
        cass.set_default_region("NA")
		color = discord.Color(value=0xf1f442)  	
    	summoner = cass.get_summoner(name=lolname)
    	check = summoner.exists
    	if check == 'False':
    		return await ctx.send("That is an invalid LoL summoner name. Check it, please! :x:")
    	em = discord.Embed(color=color, title=f'{summoner.name}')
    	em.add_field(name='Summoner Level', value=f'{summoner.level}')
    	em.add_field(name='Summoner ID', value=f'{summoner.id}')
    	em.set_thumbnail(url=f'{summoner.profile_icon.url}')
    	await ctx.send(embed=em)
